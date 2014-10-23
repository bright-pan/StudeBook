class File(models.Model):
    file_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('SbUser', blank=True, null=True)
    file_category = models.ForeignKey('SbFileCategory', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    upload_date = models.DateTimeField(blank=True, null=True)
    size = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    path = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'sb_file'