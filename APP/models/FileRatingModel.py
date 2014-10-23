class FileRating(models.Model):
    file_rating_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('SbUser', blank=True, null=True)
    file = models.ForeignKey(SbFile, blank=True, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_file_rating'