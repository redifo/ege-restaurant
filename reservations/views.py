from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservation
from .forms import ReservationForm
from django.utils import timezone
from django.contrib import messages

def make_reservation(request):
    # Initialize past and future reservations only if user is authenticated
    past_reservations = future_reservations = None
    if request.user.is_authenticated:
        past_reservations = Reservation.objects.filter(email=request.user.email, date__lt=timezone.now()).order_by('date', 'time')
        future_reservations = Reservation.objects.filter(email=request.user.email, date__gte=timezone.now()).order_by('date', 'time')
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            if request.user.is_authenticated:
                reservation.customer = request.user
                reservation.email = request.user.email
            reservation.save()
            # Redirect to the reservation_success URL with the reservation's pk
            return redirect('reservation_success', pk=reservation.pk)  # Include pk in redirect
    else:
        # Initialize the form with the email pre-filled for authenticated users
        initial_data = {'email': request.user.email} if request.user.is_authenticated else {}
        form = ReservationForm(initial=initial_data)
        if request.user.is_authenticated:
            # Hide the email field
            form.fields['email'].widget = forms.HiddenInput()

    return render(request, 'reservations.html', {
            'form': form,
            'past_reservations': past_reservations,
            'future_reservations': future_reservations
        })

def reservation_success(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    return render(request, 'reservation_success.html', {'reservation': reservation})


def edit_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservation_success', pk=reservation.pk)
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'edit_reservation.html', {'form': form, 'reservation': reservation})

def delete_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == "POST":
        reservation.delete()
        messages.success(request, 'Reservation successfully deleted.')
        return redirect('reservations')  # Redirect to a URL where you list reservations or to the home page