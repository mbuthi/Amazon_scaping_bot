### AmazonBuddy: Your Discord Companion for Product Information

Meet AmazonBuddy, your Discord companion for seamless product information extraction! This feature-rich Discord bot empowers you to effortlessly retrieve the ASIN or ISBN of a product from a link sent in a direct message. But that's not all – AmazonBuddy goes beyond identification; it can also retrieve detailed product reviews. Follow these steps to make the most of AmazonBuddy:

<p align='center'><img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMGVvZmlxNnJtaXVubmhoeWl3Nmd1cXpxeWZucDRrODdjdjZnamlyYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VD4mtzTGd3ZgEovYtr/giphy.gif" alt="Discord bot"></p>

1. **Invite the Bot:**
   ## Adding the Bot to Your Discord Server

   To integrate the bot into your Discord server, follow these simple steps:

   **Register the Bot:**
      - Navigate to the [Discord Developer Portal](https://discord.com/developers/applications).
      - Register the bot and complete the necessary setup.

   **Complete Required Information:**
      - Fill out the required details in the bot's configuration on the developer portal.

   **Invite the Bot:**
      - Once the setup is complete, use the provided invitation link to add the bot to your Discord server.


2. **Extract Product Identifiers:**
   - Send an Amazon product link to AmazonBuddy in a direct message.
   - The bot will swiftly analyze the link and respond with the corresponding ASIN or ISBN.
   - To retrieve product ASIN, use the following command:
     ```
     !asin <product_link>
     ```
   

3. **Fetch Product Reviews:**
   - To retrieve product reviews, use the following command:
     ```
     !rev <product_link>
     ```
   - AmazonBuddy will fetch and present the top positive and top critical reviews for your selected product.

4. **Fetch Product Details:**
    - To retrieve product details, use the following command:
    ```
        !info <product_link>
    ```
    - Also the product info can be extracted by:
      ```
      !info-asin <ASIN>
      ```
    - Replace `prdouct_link` with the desired link, and AmazonBuddy will provide detailed information about the corresponding product.

**Supported domains:**
- <b>".in"</b>           (India)
- <b>".com"</b>          (US)
- <b>".co.uk"</b>        (UK)
- <b>".fr"</b>           (France)
- <b>".com.mx"</b>       (Mexico)
- <b>".com.br"</b>       (Brazil)
- <b>".com.au"</b>       (Australia)
- <b><del>".com.jp       (Japan)</del>"</b>
- <b>".se"</b>           (Sweden)
- <b>".de"</b>           (Germany)
- <b>".it"</b>           (Italy)

**Important:**
- Exercise caution and use AmazonBuddy responsibly, adhering to Amazon's terms of service to avoid potential issues with website access.

**Feedback and Support:**
- If you encounter any issues or have suggestions for improvements, feel free to open an issue on the repository or submit a pull request.

**License:**
- AmazonBuddy is provided under the GPL-3.0 license. It is shared for educational purposes, and the author disclaims responsibility for any damages or legal issues arising from its use. Use it at your own risk, and thank you for choosing AmazonBuddy!
