WEBSITE_LIST = {"https://www.youtube.com/":
                {"specifics":"ablock=true;",
                 "main_menu":'refresh_sens:id;guide-icon',
                 "endpoints":
                 { 
                  "login-page":   'direct-link;signin',
                  "video":  'css selector;ytd-rich-item-renderer'
                 },
                  "sub-endpoints":
                  {
                      "main_menu":{"trending":'relies_prev:partial link text;Trending',
                                   "music":   'relies_prev:partial link text;Music',
                                   "gaming":  'relies_prev:partial link text;Gaming',
                                   "news":    'relies_prev:partial link text;News',
                                   "sports":  'relies_prev:partial link text;Sports',
                                   "learning":'relies_prev:partial link text;Learning'
                                   },
                      "trending":{"video":'rand_ind:css selector;ytd-video-renderer'
                                  },
                      "music":{"video":'rand_ind:css selector;ytd-video-renderer'
                               },
                      "gaming":{"video":"rand_ind:css selector;ytd-video-renderer"
                          
                      },
                  }
                 }
                }

WEBSITE_LIST = {"https://www.wikihow.com/":
                {"specifics":"ablock=true;",
                 "main_menu":'refresh_sens:id;header_logo',
                 "endpoints":
                 { 
                  "random_page":  "id;nav_random", #Do this a bunch of times to get a new random article multiple times
                  "login_page":  "id;nav_profile",
                  "article":  'css selector;ytd-rich-item-renderer'
                 },
             }
          }

WEBSITE_LIST = {"https://www.yelp.com/":
                {"specifics":"ablock=true;",
                 "main_menu":'refresh_sens:id;guide-icon',
                 "endpoints":
                 { 
                  "login-page":   'direct-link;signin',
                  "video":  'css selector;ytd-rich-item-renderer'
                 },
                  "sub-endpoints":
                  {
                      "main_menu":{
                      },
                  }
                 }
                }

WEBSITE_LIST = {"https://www.w3schools.com/": 
                {"specifics":"ablock=true;",
                 "main_menu": "css selector;a.w3-bar-item.w3-button.w3-hover-none.w3-left.w3-padding-16.ga-top[href='https://www.w3schools.com'][title='Home'",
                 "endpoints":
                 { 
                  "NewsLetter": 'partial link text;NEWSLETTER',
                  "Support":    'partial link text;SUPPORT',
                  "HTML":       'partial link text;Learn HTML',
                  "video":      'partial link text;Video Tutorial',
                  "Ref":        'partial link text;HTML Reference',
                  "Certd":      'partial link text;Get Certified',
                 },
                  "sub-endpoints":
                  {
                      "main_menu":{
                      },
                  }
                 }
                }

WEBSITE_LIST = {"https://www.washingtonpost.com/": 
                {"specifics":"ablock=true;",
                 "main_menu": "refresh_sens:css selector;button[data-qa='sc-header-search-menu-button'",
                 "endpoints":
                 { 
                    "AboutthePost": 'partial link text;About The Post',
                    "NewsRoom": 'partial link text;Newsroom Policies & Standards',
                 },
                  "sub-endpoints":
                  {
                      "main_menu":{   "Politics":       'relies_prev:partial link text;Politics',
                                      "Opinions":       'relies_prev:partial link text;Opinions',
                                      "World":          'relies_prev:partial link text;World',
                                      "Investigation":  'relies_prev:partial link text;Investigations',
                                      "Climate":        'relies_prev:partial link text;Climate',
                      },
                  }
                 }
                }

WEBSITE_LIST = {"https://www.godaddy.com/en-ca": 
                {"specifics":"ablock=true;",
                 "main_menu": "css selector;a[data-track-name='godaddy_logo']",
                 "endpoints":
                 { 
                    "AboutUs":   "css selector;a.mpmh0vj[data-track-name='default.aspx_link",
                    "Careers":   "css selector;a.mpmh0vj[data-track-name='careers.godaddy.com_link",
                    "ContactUs": "css selector;a.mpmh0vj[data-track-name='contact-us_link",
                    "Blog":      "css selector;a.mpmh0vj[data-track-name='_link"
                    
                 },
                  "sub-endpoints":
                  {
                      "main_menu":{   "Politics":       'relies_prev:partial link text;Politics',
                      },
                  }
                 }
                }

