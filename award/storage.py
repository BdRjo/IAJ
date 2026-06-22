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
        # نرجع المسار الكامل من Cloudinary مباشرة
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
    Storage ذكي — يكتشف نوع الملف تلقائياً:
    صورة  (jpg/png/webp/gif/svg/avif) → resource_type: image
    فيديو (mp4/webm/mov/avi/mkv)      → resource_type: video
    غير ذلك                            → resource_type: raw
    """
    IMAGE_EXT = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp', '.svg', '.tiff', '.avif'}
    VIDEO_EXT = {'.mp4', '.webm', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.m4v', '.ogv'}

    def _get_resource_type(self, name):
        ext = os.path.splitext(name)[-1].lower()
        if ext in self.IMAGE_EXT:
            return 'image'
        if ext in self.VIDEO_EXT:
            return 'video'
        return 'raw'

    def _save(self, name, content):
        resource_type = self._get_resource_type(name)
        options = {
            'resource_type': resource_type,
            'use_filename': True,
            'unique_filename': True,
            'folder': os.path.dirname(name) or '',
        }
        response = cloudinary.uploader.upload(content, **options)
        # نرجع public_id فقط — cloudinary_storage يبني الـ URL منه
        return response.get('public_id', name)
