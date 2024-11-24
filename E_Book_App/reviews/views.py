from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from E_Book_App.reviews.models import Review
from E_Book_App.books.models import Book
from E_Book_App.reviews.forms import ReviewForm, EditReviewForm, DeleteReviewForm
from E_Book_App.reviews.serializers import ReviewSerializer
from E_Book_App.reviews.permissions import IsStaffOrAdmin


class ReviewListCreateAPIView(ListCreateAPIView):
    model = Review
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    model = Review
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]


@login_required()
def review_page_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    form = ReviewForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        review = form.save(commit=False)
        review.book = book
        review.user = request.user
        review.save()
        return redirect('book-details', book.pk)

    reviews = Review.objects.filter(book=book).order_by('-created_at')
    context = {'book': book,
               'form': form}

    return render(request, 'reviews/review-page.html', context=context)


@login_required()
def edit_review_view(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    book = review.book
    form = EditReviewForm(request.POST or None, instance=review)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('book-details', book.pk)

    context = {'form': form,
               'book': book,
               'review': review}
    return render(request, 'reviews/review-edit.html', context=context)


@login_required()
def delete_review_view(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    book = review.book
    form = DeleteReviewForm(request.POST or None, instance=review)

    if request.method == 'POST' and form.is_valid():
        review.delete()
        return redirect('book-details', book.pk)

    context = {'form': form,
               'review': review}

    return render(request, 'reviews/review-delete.html', context=context)
