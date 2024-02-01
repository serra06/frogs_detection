from bing_image_downloader import downloader

query = "nissan gtr33"

downloader.download(query, limit=30, output_dir="data", timeout=60, verbose=True)