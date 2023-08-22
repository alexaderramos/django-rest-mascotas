from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework.response import Response
from rest_framework import status

from api_animalforce.settings import base


class ResponseHelper:

    @staticmethod
    def data_response(data=None, message='', status_code=status.HTTP_200_OK):
        response_data = {
            'status': True,
            'message': message,
        }
        if data is not None:
            response_data['data'] = data

        return Response(response_data, status=status_code)

    @staticmethod
    def success_response(data=None, message='Success', status_code=status.HTTP_200_OK):
        response_data = {
            'status': True,
            'message': message,
        }
        if data is not None:
            response_data['data'] = data

        return Response(response_data, status=status_code)

    @staticmethod
    def warning_response(data=None, message='Success', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY):
        response_data = {
            'status': False,
            'message': message,
        }
        if data is not None:
            response_data['data'] = data

        return Response(response_data, status=status_code)

    @staticmethod
    def error_response(errors, message='Validation Error', status_code=status.HTTP_400_BAD_REQUEST):
        response_data = {
            'status': False,
            'message': message,
            'errors': errors,
        }

        return Response(response_data, status=status_code)

    @staticmethod
    def transaction_error_response(exception, message='Transaction Error',
                                   status_code=status.HTTP_500_INTERNAL_SERVER_ERROR):
        response_data = {
            'status': False,
            'message': message,
            'exception': str(exception),
        }

        return Response(response_data, status=status_code)


class EmailHelper:
    @staticmethod
    def send(destinatario, asunto, template_path, context):
        """
        Envía un correo electrónico a la lista de destinatarios especificada.
        Utiliza una plantilla HTML personalizada para el cuerpo del correo.
        """
        html_content = render_to_string(template_name=template_path, context=context)
        msg = EmailMultiAlternatives(
            subject=asunto,
            body='',
            from_email=EmailHelper.get_from_email(),
            to=[destinatario])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    @staticmethod
    def get_from_email():
        return base.EMAIL_HOST_USER

    @staticmethod
    def send_multiple(destinatarios, asunto, template_path, context):
        """
        Envía un correo electrónico a la lista de destinatarios especificada.
        Utiliza una plantilla HTML personalizada para el cuerpo del correo.
        """
        html_content = render_to_string(template_path, context)
        msg = EmailMultiAlternatives(subject=asunto, body='', from_email=EmailHelper.get_from_email(), to=destinatarios)
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    @staticmethod
    def send_with_attach(destinatario, asunto, template_path, context, adjunto_path):
        """
        Envía un correo electrónico al destinatario especificado.
        Utiliza una plantilla HTML personalizada para el cuerpo del correo.
        Adjunta un archivo al correo electrónico.
        """
        html_content = render_to_string(template_path, context)
        msg = EmailMultiAlternatives(subject=asunto, body='', from_email=EmailHelper.get_from_email(),
                                     to=[destinatario])
        msg.attach_alternative(html_content, "text/html")
        with open(adjunto_path, 'rb') as f:
            adjunto = f.read()
        msg.attach('documento.pdf', adjunto, 'application/pdf')
        msg.send()
