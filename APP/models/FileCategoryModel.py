class FileCategory(models.Model):
    file_category_id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=45, blank=True)
    file_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_file_category'