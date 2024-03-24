from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservation
from .forms import ReservationForm
from django.utils import timezone

def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            if request.user.is_authenticated:
                reservation.customer = request.user
            reservation.save()
            # Redirect to the reservation_success URL with the reservation's pk
            return redirect('reservation_success', pk=reservation.pk)  # Include pk in redirect
    else:
        form = ReservationForm()
    return render(request, 'reservations.html', {'form': form})

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

def user_reservations(request):
    if request.user.is_authenticated:
        # Fetch reservations that are in the future
        reservations = Reservation.objects.filter(customer=request.user, date__gte=timezone.now()).order_by('date', 'time')
        return render(request, 'user_reservations.html', {'reservations': reservations})
    else:
        # Redirect to login or another appropriate page
        pass