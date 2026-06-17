"""
تخزين مخصص لرفع الفيديو على Cloudinary كـ resource_type: video
بدل ما يتعامل معاه كصورة ويرفضه
"""

from cloudinary_storage.storage import MediaCloudinaryStorage


class VideoCloudinaryStorage(MediaCloudinaryStorage):
    """Storage backend يرفع الملفات كفيديو بدل صورة"""

    def get_upload_options(self, name, content=None):
        options = super().get_upload_options(name, content)
        options['resource_type'] = 'video'
        return options
