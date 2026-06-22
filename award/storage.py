import os
import cloudinary.uploader
from cloudinary_storage.storage import MediaCloudinaryStorage


class VideoCloudinaryStorage(MediaCloudinaryStorage):
    """رفع الفيديوهات بـ resource_type: video"""
    def _save(self, name, content):
        options = {'resource_type': 'video', 'use_filename': True, 'unique_filename': True}
        response = cloudinary.uploader.upload(content, **options)
        ext = os.path.splitext(name)[-1].lower()
        return response['public_id'] + ext


class RawCloudinaryStorage(MediaCloudinaryStorage):
    """رفع ملفات PDF والمستندات بـ resource_type: raw"""
    def _save(self, name, content):
        options = {'resource_type': 'raw', 'use_filename': True, 'unique_filename': True}
        response = cloudinary.uploader.upload(content, **options)
        ext = os.path.splitext(name)[-1].lower()
        return response['public_id'] + ext


class AutoCloudinaryStorage(MediaCloudinaryStorage):
    """
    Storage ذكي — يكتشف نوع الملف تلقائياً:
    صورة  (jpg/png/webp/gif/svg) → resource_type: image
    فيديو (mp4/webm/mov/avi)     → resource_type: video
    غير ذلك                      → resource_type: raw
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
        }
        response = cloudinary.uploader.upload(content, **options)
        ext = os.path.splitext(name)[-1].lower()
        return response['public_id'] + ext
