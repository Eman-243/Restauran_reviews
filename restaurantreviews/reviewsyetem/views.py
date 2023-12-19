from django.http import HttpResponseNotFound, JsonResponse
from reviewsyetem.models import Restaurant, Comment1
from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render, redirect
from reviewsyetem.forms import CommentForm
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.decorators import login_required




def home(request):
    
    categories = Restaurant.objects.values_list('category', flat=True).distinct()
    context = {'categories': categories}
    selected_category = request.GET.get('category', '')
    if selected_category:
        restaurants = Restaurant.objects.filter(category=selected_category)
        context['selected_category'] = selected_category
    else:
        restaurants = Restaurant.objects.all()
    restaurants_with_count = []
    for restaurant in restaurants:
        comment_count = Comment1.objects.filter(restaurant_id=str(restaurant.id)).count()
        restaurant.comment_count = comment_count
        restaurants_with_count.append(restaurant)

    context['restaurants'] = restaurants_with_count

    return render(request, "reviewsyetem/home.html", context)




def details(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    comments = Comment1.objects.filter(restaurant_id=str(restaurant.id))
    context = {'restaurant': restaurant, 'comments': comments}
    return render(request, "reviewsyetem/details.html", context)




@login_required(login_url='login')
def add_review(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.restaurant_id = str(restaurant.id)
            comment.author = request.user  
            comment.save()
            return redirect('details', restaurant_id)

    else:
        form = CommentForm()

    context = {'restaurant': restaurant, 'form': form}
    return render(request, "reviewsyetem/add_review.html", context)




@login_required(login_url='login')
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment1, pk=comment_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('details', restaurant_id=comment.restaurant_id)

    else:
        form = CommentForm(instance=comment)

    context = {'form': form, 'comment': comment}
    return render(request, "reviewsyetem/edit_comment.html", context)




@login_required(login_url='login')
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment1, pk=comment_id)
    restaurant_id = comment.restaurant_id

    if request.method == 'POST':
        comment.delete()
        return JsonResponse({'message': 'Comment deleted successfully'})

    context = {'comment': comment}
    return render(request, "reviewsyetem/delete_comment.html", context)



