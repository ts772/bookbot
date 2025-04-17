try:
    import stats
    print("Stats module imported successfully!")
    print(dir(stats))  # This will show what's available in the stats module
except ImportError as e:
    print("Import failed:", e)