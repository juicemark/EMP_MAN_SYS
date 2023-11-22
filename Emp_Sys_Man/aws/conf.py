import datetime
AWS_ACCESS_KEY_ID = "AKIAU62FBHT2Q55FYV72"
AWS_SECRET_KEY = "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"
AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True

default_file_storage = 'Emp_Sys_Man.aws.utils.MediaRootS3BotoStorage'
staticfiles_storage = 'Emp_Sys_Man.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'empmansys'
S3DIRECT_REGION = 'ap-south-1'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + 'static/'
ADMIND_MEDIA_URL = MEDIA_URL + 'admin/'

two_months = datetime.timedelta(days=61)
date_two_months = datetime.date.today() + two_months
expires = date_two_months.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = {
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()),),
}
