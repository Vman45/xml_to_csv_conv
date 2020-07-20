from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings

from converter.helper_methods import process_xmls, create_dictionarys, write_csv, export_csv
from .models import Request
from .forms import RequestForm

import lxml.etree as etree
import csv
import os


def upload(request):
	if request.method == 'POST':
		# uploaded_file = request.FILES['fileList']
		print('\tREQUEST FILES:', request.FILES)
		# print('\tUPLOADED FILEEEE:', uploaded_file)
		# print('\tUPLOADED FILE:', uploaded_file.name)
		# print('t\UPLOADED FILE:', uploaded_file)

		# for file in request.FILES:
		# 	print("----------")
		# 	print("\tFILE: ", file)
	return render(request, 'converter/upload.html', {})

def home(request):
	if request.method == 'GET':
		return render(request, 'converter/home.html')
	else:
		# VARIABLES USED:
		list_data = []
		columns = []
		rows = []
		row_data = []
		filename = ''
		directory = ''
		studio = ''
		output_path = ''

		# TESTING:
		xml_list = [] 

		error_message = []

		try:
			print('\tPOST REQUEST INFO:', request.POST)
			# directory = request.POST['directory']

			directory = request.POST['directory']
			root = f'{settings.MEDIA_ROOT}\\{directory}'
			print('\t---> ROOT', root)

			studio = request.POST['studio']

			xml_list = request.POST['xml_list']
			# print('\txml_list TYPE--->', type(xml_list))
			# for filename in os.scandir(request.POST['xml_list']):
			# 	if filename.is_file() and filename.name.endswith('.xml'):
			# 		print('\tXML --> ', filename)
			

			filename = '_compiledXMLs'

			list_data = process_xmls.process_directory(root, studio)


			file_list = []
			studio_error = ''
			studio_name = ''
			

			# EXTRACT COLUMN HEADERS TO SEND TO TEMPLATE:
			columns = write_csv.extract_columns(list_data)

			# EXTRACT COLUMN ROWS
			row_data = write_csv.extract_row_data(list_data)

			# # EXPORT CSV?
			if request.POST['export'] == 'export':
				# export_csv.export_csv(columns, row_data)
				# resp = export_csv.export_csv(columns, row_data)
				# print('resp', resp)

				response = HttpResponse(content_type='text/csv')

				writer = csv.writer(response)
				writer.writerow(columns)

				for row in row_data:
					writer.writerow(row)

				response['Content-Disposition'] = f'attachment; filename="{filename}.csv"'
				return response

		
			output_path = f"C:\\Users\\nhunter\\Desktop\\code\\sandbox\\{filename}.csv"
			# output_path = directory + '\\' + "_TEST2.csv"

			write_csv.write_to_csv(filename, list_data)
		except:	
			if directory == '':
				error_message.append('PLEASE PROVIDE A DIRECTORY')
				# print('\tdir:', error_message)
			if studio == '---':
				studio = ''
				error_message.append('PLEASE PROVIDE A STUDIO')
				# print('\tstud:', error_message)
		return render(request, 'converter/home.html', {
			'directory': directory,
			'studio': studio.upper(),
			'filename': filename,
			'messages': error_message,
			'file_list': list_data,
			'columns': columns,
			'rows': row_data,
			'output_path': output_path
			}
		)


def about (request):
	return render(request, 'converter/about.html', {})
# def home(request): 
# 	all_requests = Request.objects.all
# 	return render(request, 'home.html', {'requests': all_requests})


def add_request(request):

	if request.method == 'POST':
		form = RequestForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, ('Request has been made.'))
			return redirect('home')
		else:
			messages.success(request, ('Something went wrong...'))
			return render(request, 'add_request.html', {})
	else:
		return render(request, 'converter/add_request.html', {})
