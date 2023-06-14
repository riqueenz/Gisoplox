def create():
    metrics_file_content = "0" + "\n"
    x = 1
    while x<8:
        metrics_file_content += "0" + "\n"
        x += 1
    
    metrics_file = open(".gisoplox/metrics.gisoplox", "w")
    metrics_file.write(metrics_file_content)
    metrics_file.close()
