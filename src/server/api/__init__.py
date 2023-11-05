# src/server/api/__init__.py

from supabase import create_client, Client

from .. import settings


supabase: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
