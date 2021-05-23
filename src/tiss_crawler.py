# -*- coding: utf-8 -*-
#!/usr/bin/python3

import crawl

driver_instance = crawl.crawler(True, 800, 600)

driver = driver_instance.init_driver()

driver_instance.fetch_page(driver)

driver_instance.close_driver(driver)

print ('exiting\n')
