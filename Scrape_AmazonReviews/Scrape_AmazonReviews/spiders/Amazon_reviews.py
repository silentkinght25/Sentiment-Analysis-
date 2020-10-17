import scrapy


class AmazonReviewsSpider(scrapy.Spider):
    name = 'Amazon_reviews'
    allowed_domains = ['amazon.in']
    url_list = ["https://www.amazon.in/Samsung-Galaxy-Space-Black-Storage/product-reviews/B07HGN617M/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=",
                "https://www.amazon.in/Test-Exclusive-614/product-reviews/B07HGJJ559/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber=",
                "https://www.amazon.in/Test-Exclusive-748/product-reviews/B07DJLVJ5M/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=",
                "https://www.amazon.in/Black-Storage-Additional-Exchange-Offers/product-reviews/B07PP2K69Z/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=",
                "https://www.amazon.in/Honor-Midnight-Storage-Download-Through/product-reviews/B08BSK1Q6P/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=",
                "https://www.amazon.in/Test-A6010-Dummy-Asin_39/product-reviews/B07WZG2YR3/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=",
                "https://www.amazon.in/Nokia-5-3-Android-Smartphone-64/product-reviews/B08GT299NQ/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=",
                "https://www.amazon.in/TECNO-Spark-Comet-Black-Storage/product-reviews/B08HX4RKR1/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=",
                "https://www.amazon.in/Redmi-8A-Dual-Blue-Storage/product-reviews/B07X4R63DF/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=",
                "https://www.amazon.in/Mi-A2-Blue-64GB-Storage/product-reviews/B07DJCJ9VN/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber="
                ]
    #myBaseUrl = "https://www.amazon.in/Mi-A2-Blue-64GB-Storage/product-reviews/B07DJCJ9VN/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber="
    start_urls = []
    # Creating list of urls to be scraped by appending page number a the end of base url
    for myBaseUrl in url_list: 
        for i in range(1, 100):
            start_urls.append(myBaseUrl+str(i))

    # Defining a Scrapy parser
    def parse(self, response):
        #Get the Review List
        data = response.css('#cm_cr-review_list')
            
        #Get the Name
        name = data.css('.a-profile-name')
            
        #Get the Review Title
        title = data.css('.review-title')
        #title = data.css('.a-size-base .a-link-normal .review-title .a-color-base .review-title-content .a-text-bold')
            
        # Get the Ratings
        star_rating = data.css('.review-rating')
            
        # Get the users Comments
        comments = data.css('.review-text')
        #comments = data.css('.review-text review-text-content a-size-base')
        count = 0

        
        # combining the results
        for review in star_rating:
            yield{
                'Name': ''.join(name[count].xpath(".//text()").extract()),
                'Title': ''.join(title[count].xpath(".//text()").extract()),
                'Rating': ''.join(review.xpath('.//text()').extract()),
                'Comment': ''.join(comments[count].xpath(".//text()").extract())
                }
            count=count+1
        #star_rating = response.xpath('//span[@class="a-icon-alt"]/text()').extract()
        #comments=response.xpath('//span[@class="a-size-base review-text review-text-content"]/span/text()').extract()
        #count = 0
            # create a dictionary to store the scraped info
        #scraped_data = {
         #                   'Star Rating': star_rating,
          #                  'Rating Text': comments
        #                     }
       # yield or give the scraped info to scrapy
       # yield scraped_data

