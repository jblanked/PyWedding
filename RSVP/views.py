from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm

def RSVP(request):
    success = False  # Initialize success variables

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            our_email = ''

            # special message
            email_info = f'Hey {name}, we have received your RSVP.'
            email_info_two = f"Here's their info: \n\nName: {name}\nEmail: {email}\n\nPhone Number: {subject}\n\nList of names for RSVP:\n\n{message}"

            try:
                # Send email to client
                send_mail(
                    subject='RSVP',
                    message=email_info,
                    from_email=our_email,
                    recipient_list=[email],
                    fail_silently=False,
                )

                # Send email to us
                send_mail(
                    subject="You received a RSVP for your wedding!",
                    message=email_info_two,
                    from_email=our_email,
                    recipient_list=[our_email],
                    fail_silently=False,
                )

                # Set success to True
                success = True
                

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            except Exception as e:
                return HttpResponse(f'Something went wrong: {str(e)}')

        else:
            
            # Form is invalid, render RSVP.html along with the form
            return render(request, 'RSVP.html', {'form': form})

    else:
        # GET request, render RSVP.html with a new ContactForm instance
        form = ContactForm()

    # Render the appropriate template based on the value of success
    if success:
        
        return render(request, 'success.html')
    else:
        
        return render(request, 'RSVP.html', {'form': form})
