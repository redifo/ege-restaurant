from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservation
from .forms import ReservationForm

def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            if request.user.is_authenticated:
                reservation.customer = request.user
            reservation.save()
            # Redirect to a new URL:
            return redirect('reservation_success')  
    else:
        form = ReservationForm()
    return render(request, 'reservations.html', {'form': form})

def reservation_success(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    return render(request, 'reservations/reservation_success.html', {'reservation': reservation})


def edit_reservation(request, pk):
    pass