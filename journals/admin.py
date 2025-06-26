from django.contrib import admin
from .models import JournalEntry, JournalLine

@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'description', 'branch', 'created_at')
    search_fields = ('description',)
    list_filter = ('date', 'branch')
    ordering = ('-date',)

@admin.register(JournalLine)
class JournalLineAdmin(admin.ModelAdmin):
    list_display = ('entry', 'account', 'debit', 'credit')
    list_filter = ('account',)
