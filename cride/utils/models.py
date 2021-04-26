from django.db import models 

class CRidelModel(models.Model):
    """Comparte Ride base model.

    CRideModel acts as aan abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created (DateTime): Store the datetime the object was created
        + modified (DateTime): Store the datetime the object was modified. 
    """
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.' 
    )

    modified = models.DateTimeField(
        'modified at',
        auto_add=True,
        help_text='Date time on which the object was last modified.' 
    )        

    class Meta:
        """Meta option."""
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
        
