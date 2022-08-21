#!/usr/bin/env python
# coding: utf-8

# In[24]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[5]:


slide_elem.find('div', class_='content_title')


# In[6]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[8]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[9]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[10]:


full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[11]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[12]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[13]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[16]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[17]:


df.to_html()


# In[18]:


browser.quit()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[37]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[38]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[44]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
links = browser.find_by_css('a.product-item img')

for i in range(len(links)):
    
    
    #create an empty dictionary to store img and title for each hemisphere
    hemisphere = {}
    
    #find the img and click through to next page
    browser.find_by_css('a.product-item img')[i].click()
    
    #find sample image and extract
    sample_elem = browser.links.find_by_text('Sample').first
    hemisphere['img_url'] = sample_elem['href']
    
    #get the title
    hemisphere['title'] = browser.find_by_css('h2.title').text
    
    #append list with dictionary
    hemisphere_image_urls.append(hemisphere)
    
    #we need to navigate back to the start page
    browser.back()


# In[45]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[46]:


# 5. Quit the browser
browser.quit()


# In[ ]:




