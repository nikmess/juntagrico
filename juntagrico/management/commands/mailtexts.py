from django.core.management.base import BaseCommand

from juntagrico.models import *


def get_server():
    return 'http://' + Config.adminportal_server_url()


class Command(BaseCommand):
    # entry point used by manage.py
    def handle(self, *args, **options):
        subscription = Subscription.objects.all()[0]
        if ExtraSubscription.objects.all().count() > 0:
            extrasub = ExtraSubscription.objects.all()[0]
        else:
            extrasub = None
        share = Share.objects.all()[0]
        job = RecuringJob.objects.all()[0]
        member = Member.objects.all()[0]
        depot = Depot.objects.all()[0]
        bill = Bill(ref_number='123456789', amount='1234.99')

        print('*** welcome  mit abo***')

        print(get_email_content('welcome', base_dict({
            'username': 'email@email.de',
            'password': 'password',
            'hash': 'hash',
            'subscription': subscription
        })))
        print()

        print('*** welcome  ohne abo***')

        print(get_email_content('welcome', base_dict({
            'username': 'email@email.de',
            'password': 'password',
            'hash': 'hash',
            'subscription': None
        })))
        print()

        print('*** s_created ***')

        print(get_email_content('s_created', base_dict({'share': share})))
        print()

        print('*** n_sub ***')

        print(get_email_content('n_sub', base_dict({'subscription': subscription})))
        print()

        print('*** co_welcome ***')

        print(get_email_content('co_welcome', base_dict({
            'username': 'email@email.org',
            'name': 'Hans Muster',
            'password': 'password',
            'hash': 'hash',
            'shares': '9'
        })))
        print()

        print('*** co_added ***')

        print(get_email_content('co_added', base_dict({
            'username': 'email@email.org',
            'name': 'Hans Muster',
            'password': 'password',
            'hash': 'hash',
            'shares': '9'
        })))
        print()

        print('*** password ***')

        print(get_email_content('password', base_dict({
            'email': 'email@email.org',
            'password': 'password',
        })))
        print()

        print('*** j_reminder ***')

        contact = job.type.activityarea.coordinator.get_name() + ': ' + job.type.activityarea.contact()
        print(get_email_content('j_reminder', base_dict({
            'job': job,
            'participants': [member],
            'contact': contact
        })))
        print()

        print('*** j_canceled ***')

        print(get_email_content('j_canceled', base_dict({'job': job})))
        print()

        print('*** confirm ***')

        print(get_email_content('confirm', base_dict({'hash': 'hash'})))
        print()

        print('*** j_changed ***')

        print(get_email_content('j_changed', base_dict({'job': job})))
        print()

        print('*** j_signup ***')

        print(get_email_content('j_signup', base_dict({'job': job})))
        print()

        print('*** d_changed ***')

        print(get_email_content('d_changed', base_dict({'depot': depot})))
        print()

        print('*** s_canceled ***')

        print(get_email_content('s_canceled', base_dict({
            'subscription': subscription,
            'message': 'Nachricht'
        })))
        print()

        print('*** m_canceled ***')

        print(get_email_content('m_canceled', base_dict({
            'member': member,
            'end_date': timezone.now(),
            'message': 'Nachricht'
        })))
        print()

        print('*** b_share ***')

        print(get_email_content('b_share', base_dict({
            'member': member,
            'bill': bill,
            'share': share
        })))
        print()

        print('*** b_sub ***')

        print(get_email_content('b_sub', base_dict({
            'member': member,
            'bill': bill,
            'sub': subscription,
            'start': timezone.now(),
            'end': timezone.now()
        })))
        print()

        if extrasub is not None:
            print('*** b_esub ***')

            print(get_email_content('b_esub', base_dict({
                'member': member,
                'bill': bill,
                'extrasub': extrasub,
                'start': timezone.now(),
                'end': timezone.now()
            })))
            print()
