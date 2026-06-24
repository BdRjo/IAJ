import os
import cloudinary
import cloudinary.uploader
from cloudinary_storage.storage import MediaCloudinaryStorage


class VideoCloudinaryStorage(MediaCloudinaryStorage):
    def _save(self, name, content):
        response = cloudinary.uploader.upload(
            content,
            resource_type='video',
            use_filename=True,
            unique_filename=True,
            folder=os.path.dirname(name) or '',
        )
        return response.get('public_id', name)


class RawCloudinaryStorage(MediaCloudinaryStorage):
    def _save(self, name, content):
        response = cloudinary.uploader.upload(
            content,
            resource_type='raw',
            use_filename=True,
            unique_filename=True,
            folder=os.path.dirname(name) or '',
        )
        return response.get('public_id', name)


class AutoCloudinaryStorage(MediaCloudinaryStorage):
    """
    يرفع الصور كـ image ويرجع الـ secure_url مباشرة
    عشان url() يبني الرابط الصح دايماً
    """

    def _save(self, name, content):
        try:
            response = cloudinary.uploader.upload(
                content,
                resource_type='image',
                use_filename=True,
                unique_filename=True,
                folder=os.path.dirname(name) or '',
            )
        except Exception:
            response = cloudinary.uploader.upload(
                content,
                resource_type='auto',
                use_filename=True,
                unique_filename=True,
                folder=os.path.dirname(name) or '',
            )
        # نرجع الـ secure_url مباشرة كـ name
        # هيك لما يُستدعى .url ما يحتاج يبني رابط جديد
        return response.get('secure_url', response.get('public_id', name))

    def url(self, name):
        # لو الـ name هو URL كامل، رجّعه مباشرة
        if name and (name.startswith('http://') or name.startswith('https://')):
            return name
        return super().url(name)
