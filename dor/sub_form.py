from django import forms
from mptt.forms import MoveNodeForm
from models import Taxonomy

from dor import models


class RepoSubmissionForm(forms.ModelForm):

    class Meta:
        model = models.Repository
        fields = "__all__"
        labels = {
            'name': "Name*",
            'alt_names': 'Alternate Names',
            'url': 'Url*',
            'persistent_url': 'Persistent Url*',
            'accepted_taxonomy': 'Accepted Taxonomy*',
            'accepted_content': 'Accepted Data-Types*',
            'standards': 'Standards*',
            'hosting_institution': 'Hosting Institution',
            'institution_country': 'Institution Country',
            'metadataInformationURL': 'Metadata Information URL*',
            'metadataRemarks': 'Metadata Remarks',
            'size': 'Size*',
            'date_operational': 'Date Operational*',
            'remarks': 'Remarks*',
            'db_certifications': 'Database Certificaions*',
        }
        widgets = {
            'accepted_taxonomy': forms.CheckboxSelectMultiple(),
            'accepted_content': forms.CheckboxSelectMultiple(),
            'db_certifications': forms.CheckboxSelectMultiple(),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            'metadataRemarks': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            'remarks': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }
        #exclude = ('standards','owner',)

class AnonymousRepoSubmissionForm(forms.ModelForm):

    class Meta:
        model = models.Repository
        labels = {
            'name': "Name*",
            'alt_names': 'Alternate Names',
            'url': 'Url*',
            'persistent_url': 'Persistent Url*',
            'accepted_taxonomy': 'Accepted Taxonomy*',
            'accepted_content': 'Accepted Data-Types*',
            'standards': 'Standards*',
            'hosting_institution': 'Hosting Institution',
            'institution_country': 'Institution Country',
            'metadataInformationURL': 'Metadata Information URL*',
            'metadataRemarks': 'Metadata Remarks',
            'size': 'Size*',
            'date_operational': 'Date Operational*',
            'remarks': 'Remarks*',
            'db_certifications': 'Database Certificaions*',
        }
        widgets = {
            'accepted_taxonomy': forms.CheckboxSelectMultiple(),
            'accepted_content': forms.CheckboxSelectMultiple(),
            'db_certifications': forms.CheckboxSelectMultiple(),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            'metadataRemarks': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            'remarks': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }
        exclude = ('embargoed',)


class TaxSubmissionForm(MoveNodeForm):

    class Meta:
        model = models.Taxonomy
        labels = {
            'name': 'Name*',
            'associated_content': 'Associated Content*',
            'position': 'Position*'
        }
        exclude = ('depth', 'numchild')


class ContentSubmissionForm(MoveNodeForm):

    class Meta:
        model = models.ContentType
        labels = {
            'name': 'Name*',
            'position': 'Position*'
        }
        exclude = ('lft', 'rgt', 'tree_id', 'depth')


class CertificationSubmissionForm(MoveNodeForm):

    class Meta:
        model = models.Certification
        labels = {
            'name': 'Name*',
            'position': 'Position*'
        }
        exclude = ('lft', 'rgt', 'tree_id', 'depth')


class StandardSubmissionForm(forms.ModelForm):

    class Meta:
        model = models.Standards
        fields = "__all__"
