from tools.tool import Response
import datetime
import discord
import sys
import os
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta


sys.path.append(os.getcwd())
from scrapers.scraper import Amazon




async def menu(message, user, bot = None):
    """
    Handles different commands based on the user's input message and sends corresponding information to the user via private message.

    Args:
        - message (str): The user's input message, indicating the command to be executed.
        - user (discord.User): User object representing the user who initiated the command.
        - bot (discord.Client, optional): Discord bot object. Defaults to None.

    Returns:
        - None: This function does not return any value directly. It sends relevant information to the user via private message based on the input command.
    """
    if message == '!general' or message == '!help':
        embed = discord.Embed(title = "General", description = "General overview of bot.", color = 0xff9900)
        embed.add_field(name = '!commands', value = "List of available commands and their explanation.", inline = False)
        embed.add_field(name = '!about', value = "Provides the information about the bot and its purpose.", inline = False)
        embed.add_field(name = "!ping", value = "Check the bot's response time to the server.")
        embed.add_field(name = "!status", value = "Check the status of the Amazon's server.", inline = False)
        embed.set_footer(text = 'Powered by Python', icon_url = 'https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png')
        embed.set_author(name = "Sushil", url = "https://www.github.com/sushil-rgb", icon_url = "https://avatars.githubusercontent.com/u/107347115?s=400&u=7a5fbfe85d59d828d52b407c999474c8938325c7&v=4")
        embed.timestamp = datetime.now()

        await user.send(embed = embed)

    if message == '!commands':
        embed = discord.Embed(title ='Bot menu', description = "List of available commands and their explanation.", color = 0xff9900)
        embed.add_field(name = "!asin `https://www.amazon.com/PlayStation-5-Console-CFI-1215A01X/dp/B0BCNKKZ91`", value = "Extracts ASIN from the provided product link.", inline = False)
        embed.add_field(name = "!rev `https://www.amazon.com/PlayStation-5-Console-CFI-1215A01X/dp/B0BCNKKZ91`", value = "Extracts the top positive and top critical review of the product.", inline = False)
        embed.add_field(name = "!info `https://www.amazon.com/PlayStation-5-Console-CFI-1215A01X/dp/B0BCNKKZ91`", value = "Extracts the detailed product informations.", inline = False)
        embed.add_field(name = "!info-asin `B0BCNKKZ91`", value = "Extracts the detailed product informations.", inline = False)
        embed.set_footer(text = 'Powered by Python', icon_url = 'https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png')
        embed.set_author(name = "Sushil", url = "https://www.github.com/sushil-rgb", icon_url = "https://avatars.githubusercontent.com/u/107347115?s=400&u=7a5fbfe85d59d828d52b407c999474c8938325c7&v=4")
        embed.timestamp = datetime.now()

        await user.send(embed = embed)

    if message == '!about':
        embed = discord.Embed(title = "About", description = "Provides the information about the bot and its purpose.", color = 0xff9900)
        embed.add_field(name = "Purpose", value = "The purpose of this bot is to extract product ASIN and product reviews by product link, and retrieve product information by pasting ASIN.", inline = False)
        embed.add_field(name = "Example Usage:",
                        value = "!asin `[product link]` - Extracts ASIN from the provided product link. \n"
                                "!rev `[product link]` - Extracts product reviews from the provided product link. \n"
                                "!info `[product link]` - Retrieves detailed product information using the provided link. \n"
                                "!info-asin `[ASIN]` - Retrieves detailed product information using the provided ASIN. \n",
                        inline = False
                        )
        embed.set_footer(text = 'Powered by Python', icon_url = 'https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png')
        embed.set_author(name = "Sushil", url = "https://www.github.com/sushil-rgb", icon_url = "https://avatars.githubusercontent.com/u/107347115?s=400&u=7a5fbfe85d59d828d52b407c999474c8938325c7&v=4")
        embed.timestamp = datetime.now()

        await user.send(embed = embed)

    if message == '!ping':
        latency = bot.latency
        embed = discord.Embed(title = "Ping",
                              description = f"Pong! Bot latency is {latency * 1000:.2f}ms.",
                              color = 0x008000,
                              )
        embed.set_footer(text = 'Powered by Python', icon_url = 'https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png')
        embed.set_author(name = "Sushil", url = "https://www.github.com/sushil-rgb", icon_url = "https://avatars.githubusercontent.com/u/107347115?s=400&u=7a5fbfe85d59d828d52b407c999474c8938325c7&v=4")
        embed.timestamp = datetime.now()

        await user.send(embed = embed)


    if message == '!status':
        repsonse = await Response('https://www.amazon.com').response()
        if repsonse == 200:
            embed = discord.Embed(title = "Status", description = f'Status code: 200', color = 0x008000)
            embed.set_footer(text = 'Powered by Python', icon_url = 'https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png')
            embed.set_author(name = "Sushil", url = "https://www.github.com/sushil-rgb", icon_url = "https://avatars.githubusercontent.com/u/107347115?s=400&u=7a5fbfe85d59d828d52b407c999474c8938325c7&v=4")
            embed.timestamp = datetime.now()

            await user.send(embed = embed)
        else:
            embed = discord.Embed(title = "Status", description = repsonse, color = 0xFF0000)
            embed.set_footer(text = 'Powered by Python', icon_url = 'https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png')
            embed.set_author(name = "Sushil", url = "https://www.github.com/sushil-rgb", icon_url = "https://avatars.githubusercontent.com/u/107347115?s=400&u=7a5fbfe85d59d828d52b407c999474c8938325c7&v=4")
            embed.timestamp = datetime.now()

            await user.send(embed = embed)


async def on_ready(scheduler):
    """
    This function prints a message when the bot is ready to use.
    """
    # scheduler.start()
    print(f"Buddy is now running.")
     
    


async def asin_isbn(userInput, user):
    """
    This function takes a user object and a user input as parameters, calls the Amazon class to get ASIN and ISBN numbers,
    and sends the results to the user.

    Args:
        -user (discord.User): User object.
        -userInput (str): User input.

    Returns:
        -None
    """
    datas = await Amazon(userInput).getASIN()
    await user.send(datas)


async def getdataByLink(userInput, user):
    """
    This function takes a user input and a suer object as parameters, call the Amazon class to get product data using ASIN,
    creates a discord embed with the product data, and send the embed to the user.

    Args:
        -userInput (str): User input.
        -user (discord.User): User object.

    Returns:
        -None
    """
    try:
        datas = await Amazon(userInput).dataByLink()
        name = datas['Name']
        hyperlink = datas['Hyperlink']
        embed = discord.Embed(title = name, url = hyperlink, color = 0xff9900)
        embed.add_field(name = 'Price', value = datas['Price'], inline = False)
        embed.add_field(name = 'Availability', value = datas['Availability'], inline = False)
        embed.add_field(name = "Store", value = f"[{datas['Store']}]({datas['Store link']})", inline = False)
        embed.add_field(name = 'Rating', value = datas['Rating'], inline = False)
        embed.add_field(name = 'Review count', value = datas['Rating count'], inline = False)
        embed.set_thumbnail(url = datas['Image'])
        embed.timestamp = datetime.now()
        embed.set_footer(text = 'Powered by Python', icon_url = 'https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png')
        await user.send(embed = embed)
    except Exception as e:
        print(e)
        await user.send(f'Content loading error. Please try again in few minutes.')

async def getDataByAsinSearch(scheduler, userInput, channel):
    links_to_pages = await Amazon(userInput).find_links_with_aria_label()
    links_to_pages.insert(0, userInput)
    
    # file path
    file_path = "scraped.txt"
    
    # Check if file exists. If not, create it.
    if not os.path.exists(file_path):
        open(file_path, 'a').close()
    
    in_text_file = []
    
    # Read file to retrieve asins
    with open("scraped.txt", "r") as file:
        in_text_file = file.readlines()
    
    # Remove leading and trailing spaces
    in_text_file = [asin_p.strip() for asin_p in in_text_file]
    
    for link_to_page in links_to_pages:
        await channel.send(f'__**Page {links_to_pages.index(link_to_page) + 1}**__')  # Bold and underlined text
        try:        
            data_asins = await Amazon(link_to_page).product_links()            
            for asin in data_asins:  
                
                if asin in in_text_file:
                    continue
                with open("scraped.txt", "a") as file:
                    file.write(f"{asin}\n")
                await getdataByASIN(asin, channel)            
        except Exception as e:
            print(f"Error {e}")        
            await channel.send(f'Content loading error. Please try again in few minutes.')
    scheduler.add_job(
        getDataByAsinSearch, 
        'date', 
        run_date=datetime.utcnow() + timedelta(minutes=10), 
        args=[scheduler, userInput, channel]
    )   
    await channel.send(f'__**Rescraping...**__')  # Bold and underlined text 
    

async def getdataByASIN(userInput, user):
    """
    This function takes a user input and a suer object as parameters, call the Amazon class to get product data using ASIN,
    creates a discord embed with the product data, and send the embed to the user.

    Args:
        -userInput (str): User input.
        -user (discord.User): User object.

    Returns:
        -None
    """
    try:
        datas = await Amazon(userInput).dataByAsin()              
        name = datas['Name']
        hyperlink = f"https://www.amazon.com/dp/{datas['Hyperlink']}"
        embed = discord.Embed(title = name, url = hyperlink, color = 0xff9900)
        embed.add_field(name = 'Price', value = datas['Price'], inline = False)
        embed.add_field(name = 'Availability', value = datas['Availability'], inline = False)
        embed.add_field(name = "Store", value = f"[{datas['Store']}]({datas['Store link']})", inline = False)
        embed.add_field(name = 'Rating', value = datas['Rating'], inline = False)
        embed.add_field(name = 'Review count', value = datas['Rating count'], inline = False)
        embed.set_thumbnail(url = datas['Image'])
        embed.timestamp = datetime.now()
        embed.set_footer(text = 'Powered by Python', icon_url = 'https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png')
        await user.send(embed = embed)
    except Exception as e:
        print(f"Error 2 {e}")
        await user.send(f'Content loading error. Please try again in few minutes.')


async def productReview(userInput, user):
    """
    This function takes a user input and a suer object as parameters, call the Amazon class to get product reviews using product link,
    creates a discord embed with the product reviews, and send the embed to the user.

    Args:
        -userInput (str): User input.
        -user (discord.User): User object.

    Returns:
        -None
    """
    try:
        amazon = Amazon(userInput)
        asin = await amazon.getASIN()
        datas = await amazon.product_review()
        review_url = f"https://www.amazon.com/product-reviews/{asin}"
        if isinstance(datas, dict):
            positive_review = datas['top positive review']['review']
            critcal_review = datas['top critical review']['review']

            # Create Discord embed for top positive review:
            positive_embed = discord.Embed(title = "Top positive review", url = userInput, color = 0x008000)
            positive_embed.add_field(name = "Product", value = datas['top positive review']["product"], inline = False)
            positive_embed.add_field(name = "Customer", value = datas['top positive review']['customer'])
            positive_embed.add_field(name = "Stars", value = datas['top positive review']['stars'], inline = False)
            positive_embed.add_field(name = "Title", value = datas['top positive review']['title'], inline = False)
            if len(positive_review) >= 150:
                positive_embed.add_field(name = "Review", value = f"""{datas['top positive review']['review'][:150]}...""", inline = False)
                positive_embed.add_field(name = "Read more", value = f"[Full Review]({review_url})", inline = False)
            else:
                positive_embed.add_field(name = "Review", value = datas['top positive review']['review'])
            positive_embed.set_thumbnail(url = datas["top positive review"]['image'])
            positive_embed.timestamp = datetime.now()
            positive_embed.set_footer(text = 'Powered by Python', icon_url = 'https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png')
            await user.send(embed = positive_embed)

            # Create Discord embed for top critical review:
            critical_embed = discord.Embed(title = "Top critical review", url = userInput, color = 0xFF0000)
            critical_embed.add_field(name = "Product", value = datas['top critical review']["product"], inline = False)
            critical_embed.add_field(name = "Customer", value = datas['top critical review']['customer'])
            critical_embed.add_field(name = "Stars", value = datas['top critical review']['stars'], inline = False)
            critical_embed.add_field(name = "Title", value = datas['top critical review']['title'], inline = False)
            if len(critcal_review) >= 150:
                critical_embed.add_field(name = "Review", value = f"""{datas['top critical review']['review'][:150]}...""", inline = False)
                critical_embed.add_field(name = "Read more", value = f"[Full Review]({review_url})", inline = False)
            else:
                critical_embed.add_field(name = "Review", value = datas['top critical review']['review'])
            critical_embed.set_thumbnail(url = datas["top critical review"]['image'])
            critical_embed.timestamp = datetime.now()
            critical_embed.set_footer(text = 'Powered by Python', icon_url = 'https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png')
            await user.send(embed = critical_embed)
        else:
            embed = discord.Embed(title = datas, url = userInput, color = 0xFF0000)
            await user.send(embed = embed)
    except Exception as e:
        await user.send(f"Content loading error. Please try again in few minutes.")

