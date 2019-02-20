from django.db import models

class House(models.Model):
    watcher_first_name = models.CharField(max_length=50)
    watcher_last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    longitude = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    #site info
    surround_options = (
        ('T', 'Trail'),
        ('D', 'Dirt Road'),
        ('P', 'Paved Road'),
        ('N', 'None'),
    )
    surr_corr = models.CharField("Surrounding Corridors", max_length=1, choices=surround_options)
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
    surrounding_structures = models.CharField(max_length=2, choices=struct_choices)
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
    surrounding_water_resources = models.CharField(max_length=2, choices=wat_choices)
    t_f_choices = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    noise = models.CharField("Noise Pollution", max_length=1, choices=t_f_choices)
    deg_options = (
        ('TD', 'Trash Dumping'),
        ('ER', 'Erosion'),
        ('IS', 'Invasive Species'),
        ('NO', 'None'),
    )
    hab_deg = models.CharField("Habitat Degradation", max_length=2, choices=deg_options)
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
    hab_typ = models.CharField("Habitat Type", max_length=2, choices=habitat_type)
    prop_type = models.CharField("Property Type", max_length=2, choices=property_type)
    slope_choices = (
        ('F', 'Flat'), 
        ('G', 'Gentle'), 
        ('U', 'Undulating'), 
        ('S', 'Steep'), 
    )
    slope = models.CharField(max_length=1, choices=slope_choices)
    #habitat features
    successional = (
        ('ES', 'Early Successional'),
        ('LS', 'Late Successional'),
    )
    habitat_trees = (
        ('CON', 'Coniferous'),
        ('DEC', 'Deciduous'),
    )
    con_dec = models.CharField("Coniferous or Deciduous Trees", max_length=3, choices=habitat_trees)
    habitat_features = models.CharField("Early or Late Successional", max_length=2, choices=successional)
    other_features = models.TextField()
    #stats
    size_choices = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    size = models.CharField("Size of House", max_length=1, choices=size_choices)
    sun_choices = (
        ('AN', 'Almost None'),
        ('VL', 'Very Little'),
        ('SM', 'Some'),
        ('PL', 'Plenty'),
        ('EX', 'Excessive'),
    )
    morn_sun  = models.CharField("Access to Morning Sunlight", max_length=2, choices=sun_choices)
    aft_sun = models.CharField("Access to Afternoon Sunlight", max_length=2, choices=sun_choices) 
    num_chambers = models.PositiveIntegerField("Number of Chambers")
    ground_height = models.PositiveIntegerField("Height Above Ground")
    water_dist = models.PositiveIntegerField("Distance to Water")
    mount_choices = (
        ('BD', 'Building'),
        ('TR', 'Tree'),
        ('PL', 'Pole'), 
    )
    mount_on = models.CharField( max_length=2, choices=mount_choices)
    installation_date = models.DateField()
    color = models.CharField(max_length=50)
    
