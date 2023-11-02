from django.urls import resolve
from django.views.generic.base import TemplateResponseMixin
from typing import Sequence


class TemplateLocationMixin(TemplateResponseMixin):
    template_location = None

    def get_namespace(self) -> str:
        """get the namespace base from the current path.

        Returns
        -------
        str
            /blogger/profile converted to app:blogger:profile
        """
        return resolve(self.request.path).namespace

    def get_template_location(self) -> str:
        """get the template location base from the url namespace.
        location of template should conform with the location url

        Returns
        -------
        str
            Folder path url namespace with ':' replaced with '/'
            /blogger/profile converted to app:blogger:profile
            then covert again to app/blogger/profile
        """
        namespace = self.get_namespace()
        return namespace.replace(":", "/")

    def get_base_location(self) -> str:
        """get the base location from the extracted namespace.

        Returns
        -------
        str
            the location of the base/partial templates
        """
        namespace = self.get_namespace()
        return "/".join(namespace.split(":")[0:2])

    def get_template(self) -> str:
        """get the location of the render to be rendered.
        'template_location' specifies the location allowing reuse of template.

        Returns
        -------
        str
            the path of template
        """
        if self.template_location:
            return f"{ self.template_location }/{ self.template_name }"
        else:
            return f"{ self.get_template_location() }/{ self.template_name }"
