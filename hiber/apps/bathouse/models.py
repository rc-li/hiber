from django import forms
from django.db import models
from django.contrib.postgres.fields import (ArrayField, FloatRangeField,
                                            IntegerRangeField)
from wagtail.admin.edit_handlers import (MultiFieldPanel, FieldRowPanel,
                                         FieldPanel)
from wagtail.images.edit_handlers import ImageChooserPanel


class ChoiceArrayField(ArrayField):
    """
    A field that allows us to store an array of choices.
    Uses Django's Postgres ArrayField
    and a MultipleChoiceField for its formfield.
    """

    def formfield(self, **kwargs):
        defaults = {
            'form_class': forms.MultipleChoiceField,
            'choices': self.base_field.choices,
        }
        defaults.update(kwargs)
        # Skip our parent's formfield implementation completely as we don't
        # care for it.
        # pylint:disable=bad-super-call
        return super(ArrayField, self).formfield(**defaults)


class Bat(models.Model):
    """
    Describes a model that has all the traits for a bat.

    This is consumed on the front-end to show species of bats to the user,
    as well as a way to tag what bats were seen at a particular House.
    """
    common_name = models.CharField(
        max_length=255, help_text="Name used in everyday life")
    scientific_name = models.CharField(
        max_length=255, help_text="Formal system used for naming species")

    RARITY_CHOICES = (('CO', 'Common'), ('SC', 'Seasonally Common'), ('RA',
                                                                      'Rare'))

    rarity = models.CharField(
        max_length=2,
        choices=RARITY_CHOICES,
        default='CO',
        help_text="How often the species is seen")

    HABIT_CHOICES = (('HI', 'Hibernates'), ('MI', 'Migrates'),
                     ('CR', 'Cave roosts'), ('TR', 'Tree roosts'))

    habits = ChoiceArrayField(
        models.CharField(max_length=2, choices=HABIT_CHOICES),
        blank=True,
        help_text="What the species tends to do in order to survive")

    size = FloatRangeField(help_text="Typical size in inches")
    pups = IntegerRangeField(help_text="Typical offspring per year")

    RISK_CHOICES = (('NT', 'Not threatened'), ('EN', 'Endangered'),
                    ('TH', 'Threatened'), ('SC', 'Special concern'))

    risk = ChoiceArrayField(
        models.CharField(max_length=2, choices=RISK_CHOICES),
        blank=True,
        help_text="Conservation status for the species")

    SCOPE_CHOICES = (('ST', 'State'), ('FE', 'Federally'))

    risk_scope = ChoiceArrayField(
        models.CharField(max_length=2, choices=SCOPE_CHOICES, null=True),
        blank=True,
        null=True,
        help_text="Whether or not this applies at the federal or state level")

    bat_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    panels = [
        MultiFieldPanel([
            FieldPanel('common_name', classname="col12"),
            FieldPanel('scientific_name', classname="col12"),
        ],
                        heading="Identification",
                        classname="collapsible"),
        MultiFieldPanel([
            FieldPanel('rarity', classname="col12"),
            FieldPanel(
                'habits',
                classname="col12",
                widget=forms.CheckboxSelectMultiple),
            FieldPanel(
                'risk', classname="col12",
                widget=forms.CheckboxSelectMultiple),
            FieldPanel(
                'risk_scope',
                classname="col12",
                widget=forms.CheckboxSelectMultiple),
        ],
                        heading="Information",
                        classname="collapsible"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('size', classname="col6"),
                FieldPanel('pups', classname="col6"),
            ])
        ],
                        heading="Characteristics",
                        classname="collapsible"),
        ImageChooserPanel('bat_image')
    ]

    def __str__(self):
        return f"{self.common_name} ({self.scientific_name})"


class House(models.Model):
    watcher_first_name = models.CharField(max_length=50)
    watcher_last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    longitude = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    # site info
    surround_options = (
        ('T', 'Trail'),
        ('D', 'Dirt Road'),
        ('P', 'Paved Road'),
        ('N', 'None'),
    )
    surr_corr = models.CharField(
        "Surrounding Corridors", max_length=1, choices=surround_options)
    geog_choices = (
        ('VA', 'Valley'),
        ('HP', 'Hillside / Pond'),
        ('RP', 'Ridgetop Plane'),
    )
    geography = models.CharField(max_length=2, choices=geog_choices)
    struct_choices = (
        ('BU', 'Building'),
        ('BR', 'Bridge'),
        ('SI', 'Sign'),
        ('DA', 'Dam'),
        ('NO', 'None'),
    )
    surrounding_structures = models.CharField(
        max_length=2, choices=struct_choices)
    wat_choices = (
        ('RI', 'River'),
        ('ES', 'Ephemeral Stream'),
        ('PS', 'Permanent Stream'),
        ('LA', 'Lake'),
        ('PO', 'Pond'),
        ('VP', 'Vernal Pool'),
        ('IW', 'Inland Wetland'),
        ('CW', 'Coastal Wetland'),
        ('NO', 'None'),
    )
    surrounding_water_resources = models.CharField(
        max_length=2, choices=wat_choices)
    t_f_choices = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    noise = models.CharField(
        "Noise Pollution", max_length=1, choices=t_f_choices)
    deg_options = (
        ('TD', 'Trash Dumping'),
        ('ER', 'Erosion'),
        ('IS', 'Invasive Species'),
        ('NO', 'None'),
    )
    hab_deg = models.CharField(
        "Habitat Degradation", max_length=2, choices=deg_options)
    property_type = (
        ('TO', 'Town'),
        ('ST', 'State'),
        ('SC', 'School'),
        ('LA', 'Land'),
        ('TR', 'Trust'),
        ('PR', 'Private'),
    )
    habitat_type = (
        ('FE', 'Forest Edge'),
        ('WP', 'Wetland/Pond'),
        ('FI', 'Field'),
        ('RI', 'Riparian'),
        ('DA', 'Developed Area'),
        ('FG', 'Forest Gap'),
    )
    hab_typ = models.CharField(
        "Habitat Type", max_length=2, choices=habitat_type)
    prop_type = models.CharField(
        "Property Type", max_length=2, choices=property_type)
    slope_choices = (
        ('F', 'Flat'),
        ('G', 'Gentle'),
        ('U', 'Undulating'),
        ('S', 'Steep'),
    )
    slope = models.CharField(max_length=1, choices=slope_choices)
    # habitat features
    successional = (
        ('ES', 'Early Successional'),
        ('LS', 'Late Successional'),
    )
    habitat_trees = (
        ('CON', 'Coniferous'),
        ('DEC', 'Deciduous'),
    )
    con_dec = models.CharField(
        "Coniferous or Deciduous Trees", max_length=3, choices=habitat_trees)
    habitat_features = models.CharField(
        "Early or Late Successional", max_length=2, choices=successional)
    other_features = models.TextField()
    # stats
    size_choices = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    size = models.CharField(
        "Size of House", max_length=1, choices=size_choices)
    sun_choices = (
        ('AN', 'Almost None'),
        ('VL', 'Very Little'),
        ('SM', 'Some'),
        ('PL', 'Plenty'),
        ('EX', 'Excessive'),
    )
    morn_sun = models.CharField(
        "Access to Morning Sunlight", max_length=2, choices=sun_choices)
    aft_sun = models.CharField(
        "Access to Afternoon Sunlight", max_length=2, choices=sun_choices)
    num_chambers = models.PositiveIntegerField("Number of Chambers")
    ground_height = models.PositiveIntegerField("Height Above Ground")
    water_dist = models.PositiveIntegerField("Distance to Water")
    mount_choices = (
        ('BD', 'Building'),
        ('TR', 'Tree'),
        ('PL', 'Pole'),
    )
    mount_on = models.CharField(max_length=2, choices=mount_choices)
    installation_date = models.DateField()
    color = models.CharField(max_length=50)
