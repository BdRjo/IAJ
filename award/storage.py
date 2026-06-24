import os
import cloudinary
import cloudinary.uploader
from cloudinary_storage.storage import MediaCloudinaryStorage


class VideoCloudinaryStorage(MediaCloudinaryStorage):
    """رفع الفيديوهات بـ resource_type: video"""
    def _save(self, name, content):
        options = {
            'resource_type': 'video',
            'use_filename': True,
            'unique_filename': True,
            'folder': os.path.dirname(name) or '',
        }
        response = cloudinary.uploader.upload(content, **options)
        return response.get('public_id', name)


class RawCloudinaryStorage(MediaCloudinaryStorage):
    """رفع ملفات PDF والمستندات بـ resource_type: raw"""
    def _save(self, name, content):
        options = {
            'resource_type': 'raw',
            'use_filename': True,
            'unique_filename': True,
            'folder': os.path.dirname(name) or '',
        }
        response = cloudinary.uploader.upload(content, **options)
        return response.get('public_id', name)


class AutoCloudinaryStorage(MediaCloudinaryStorage):
    """
    Storage للصور فقط — يرفع كل شيء كـ image
    يُستخدم كـ default storage
    """
    def _save(self, name, content):
        options = {
            'resource_type': 'image',
            'use_filename': True,
            'unique_filename': True,
            'folder': os.path.dirname(name) or '',
        }
        try:
            response = cloudinary.uploader.upload(content, **options)
            return response.get('public_id', name)
        except Exception:
            # لو فشل كـ image، جرب كـ auto
            options['resource_type'] = 'auto'
            response = cloudinary.uploader.upload(content, **options)
            return response.get('public_id', name)
