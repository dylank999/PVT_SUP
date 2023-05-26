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
                  "Review":  'partial link text;Write a Review',
                  "About":   'partial link text;About Yelp',
                  "Career":  'partial link text;Careers',
                  "Events":  'partial link text;Events',
                  "Talk":    'partial link text;Talk',
                  "Support": 'partial link text; Support',
                  "Develop": 'partial link text;Developers',
                  "Privacy": 'partial link text;Privacy Policy',
                  
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
                    "AboutUs":       "css selector;a.mpmh0vj[data-track-name='default.aspx_link",
                    "Careers":       "css selector;a.mpmh0vj[data-track-name='careers.godaddy.com_link",
                    "ContactUs":     "css selector;a.mpmh0vj[data-track-name='contact-us_link",
                    "Blog":          "css selector;a.mpmh0vj[data-track-name='_link",
                    "Legal":         "css selector; a.mpmh0vj[data-track-name='agreements_link",
                    "StartForFree":  "partial link text;Start for Free"

                 }
                 }
                }

WEBSITE_LIST = {"https://www.etsy.com/": 
                {"specifics":"ablock=true;",
                 "main_menu": "refresh_sens:css selector;button[data-qa='sc-header-search-menu-button'",
                 "endpoints":
                 { 
                    "HomeFav":   "partial link text;Home Favourites",
                    "Jewellery": "partial link text;Jewellery & Accessories",
                    "Clothing":  "partial link text;Clothing & Shoes",
                    "HomeLiving":"partial link text;Home & Living",
                    "Wedding":   "partial link text;Wedding & Party",
                    "ToysEnt":   "partial link text;Toys & Entertainment",
                    "Art":       "partial link text;Art & Collectibles",
                    
                 }
                 }
                }

WEBSITE_LIST = {"https://en.softonic.com/": 
                {"specifics":"ablock=true;",
                 "main_menu": "refresh_sens:css selector;button[data-qa='sc-header-search-menu-button'",
                 "endpoints":
                 { 
                    "Apps":   "css selector;ul.menu-featured__list > li.menu-featured__item:nth-child(1) > a.menu-featured__link",
                    "Games":  "css selector;ul.menu-featured__list > li.menu-featured__item:nth-child(2) > a.menu-featured__link",
                    "News":   "css selector;ul.menu-featured__list > li.menu-featured__item:nth-child(3) > a.menu-featured__link",
                    "Roblox": "partial link text;Roblox games",
                    "Chrome": "partial link text;Chrome extensions"
                 }
                 }
                }

WEBSITE_LIST = {"https://9gag.com/": 
                {"specifics":"ablock=true;",
                 "main_menu": "refresh_sens:css selector;.menu",
                 "endpoints":
                 { 
                    "Shuffle": "partial link text;Shuffle",#This is another randomizer built into the site so you could run it a few times if you wanted 
                    "GetApp": "partial link text;Get App",
                    "Memeland":"partial link text;Memeland",
                    "Cringe": "partial link text;Potatoz",
                    "Captain": "partial link text;Captainz",

 
                 },
                  "sub-endpoints":
                  {
                      "main_menu":{   "Home":     'relies_prev:partial link text;Home',
                                      "Trending": 'relies_prev:partial link text;Trending',
                                      "Fresh":    'relies_prev:partial link text;Fresh',
                                      "Top":      'relies_prev:partial link text;Top',
                                      "Schawb":   'relies_prev:partial link text;Girl',
                      },
                  }
                 }
                }


WEBSITE_LIST = {"https://williscollege.com/": 
                {"specifics":"ablock=true;",
                 "main_menu": "refresh_sens:css selector;div.x-anchor.x-anchor-toggle.has-graphic.e12395-e56.m9kb-y.m9kb-11.m9kb-13.m9kb-14.m9kb-15.m9kb-16.m9kb-18.m9kb-1b.m9kb-1e.m9kb-1g",
                 "endpoints":
                 { 
                    "Events":    "partial link text;Business",
                    "Business":   "partial link text;Business",
                    "Technology": "partial link text;Technology",
                    "Healthcare":  "partial link text;Health Care",
 
                 },
                  "sub-endpoints":
                  {
                      "main_menu":{   "Home":     'relies_prev:partial link text;Home',

                      },
                  }
                 }
                }

WEBSITE_LIST = {"https://www.bankofamerica.com/": 
                {"specifics":"ablock=true;",
                 "checking_menu": "refresh_sens:css selector;ul.main-nav-links li:nth-child(1)",
                 "savings_menu":  "refresh_sens:css selector;ul.main-nav-links li:nth-child(2)",
                 "credit_menu":   "refresh_sens:css selector;ul.main-nav-links li:nth-child(3)",
                 "auto_menu":     "refresh_sens:css selector;ul.main-nav-links li:nth-child(5)",
                 "endpoints":
                 { 
                   
                 },
                  "sub-endpoints":
                  {
                      "checking_menu":{  "Online": 'relies_prev:partial link text;Online Banking' ,
                                         "Mobile": 'relies_prev:partial link text;Mobile Banking',
                                         "Debit":  'relies_prev:partial link text;Debit Card',
                                         "Advntg": 'relies_prev:partial link text;Bank of America Advantage Banking',
                                         "Student":'relies_prev:partial link text;Student Banking',

                      },

                      "savings_menu":{  "Online": 'relies_prev:partial link text;Bank of America Advantage Savings' ,
                                         "IRAs": 'relies_prev:partial link text;IRAs',
        
                      },

                       "credit_menu":{  "CredCrds": 'relies_prev:partial link text;Cash Back Credit Cards' ,
                                         "Travel":  'relies_prev:partial link text;Travel and Airlines Rewards Cards',
                                         "LowerIn": 'relies_prev:partial link text;Lower Interest Rate Cards',
                                         "Points":  'relies_prev:partial link text;Points Rewards Cards',
                                         "Rebuild": 'relies_prev:partial link text;Cards to Build or Rebuild Credit',
                                         "Studnet": 'relies_prev:partial link text;Cards for Students',
        
                      },

                       "auto_menu":{  "LoanR": 'relies_prev:partial link text;Check auto loan rates' ,
                                      "LoanC": 'relies_prev:partial link text;Use the auto loan calculator',
                                      "Shop":  'relies_prev:partial link text;Shop for a car',
                                      "Apply": 'relies_prev:partial link text;Apply for an auto loan',

        
                      },
                  }
                 }
                }
