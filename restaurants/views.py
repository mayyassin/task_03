from django.shortcuts import render

def welcome(request):
	return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

	rest_list = [
		{
			'restaurant_name': 'stack',
			'food_type': 'burgers'
		},
		{
			'restaurant_name': 'pf changs',
			'food_type': 'Chinese'
		},
		{
			'restaurant_name': 'Ashaz',
			'food_type': 'Indian'
		},
	]
	context = {
				"my_list": rest_list,
	}
	return render(request, 'list.html', context)


def restaurant_detail(request):

	rest_detail = {
		'restaurant_name': 'Maki',
		'food_type': 'sushi'
	}

	context = {
				"my_object": rest_detail,

	}
	return render(request, 'detail.html', context)
