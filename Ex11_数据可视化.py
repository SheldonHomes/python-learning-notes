"""
使用matplotlib绘制2004-2024年编程语言排名的折线图

具体要求：
1. 从https://www.tiobe.com/tiobe-index/ 中获取2004-2024年编程语言排名的HTML数据
2. 通过网站获取的HTML内容，解析数据，获取编程语言名称和排名数据
3. 使用matplotlib绘制折线图，横坐标为年份，纵坐标为排名，折线图的颜色为蓝色，线宽为2

知识引导：
1. JSON文件
    JSON文件是一种轻量级的数据交换格式，它基于JavaScript的一个子集，易于人阅读和编写，同时也易于机器解析和生成。
    主要功能：负责不同编程语言、操作系统、数据库、框架等之间的数据传递与交互
    格式要求：
    ①数据结构：
        使用对象（用花括号{}表示）和数组（用方括号[]表示）来组织数据。
        对象包含键值对，键必须是字符串，值可以是字符串、数字、布尔值、数组、对象或null。
    ②字符串：
        字符串必须用双引号括起来，单引号不被接受。
        字符串中不能包含未转义的控制字符，如换行符。
    ③数字：
        可以是整数或浮点数，但不能有前导零（例如，01是无效的）。
    ④布尔值和null：
        布尔值使用true和false（小写），null表示空值。
    ⑤无注释：
        JSON不允许使用注释，所有的内容必须是有效的数据。
    ⑥编码：
        JSON文本必须是UTF-8编码。
    例：
    {
        "name": "Alice",
        "age": 30,
        "is_student": false,
        "courses": ["Math", "Science"],
        "address": {
            "city": "Wonderland",
            "zip": null
        }
    }
    Python数据与JSON数据之间的转换：使用json模块
        json.load()：将JSON格式的字符串转换为Python对象
        json.dump()：将Python对象转换为JSON格式的字符串

2. 网络请求与响应
    网络请求：客户端向服务器发送请求，获取资源或执行操作。
    主要功能：发送GET、POST、PUT、DELETE等请求，处理响应数据，设置请求头、参数、代理等。
    请求包含请求行、请求头、请求体三部分，响应包含状态行、响应头、响应体三部分。
    请求方法：
        GET
        用途：用于请求获取资源（如网页、图像等）。
        特点：
            不改变服务器上的任何资源（安全性）。
            可以在URL中包含查询参数，通常用于读取数据。
            请求内容会被缓存，有长度限制（URL长度）。
        POST
        用途：用于向服务器提交数据（如表单数据、文件上传等）。
        特点：
            通常会改变服务器上的资源（如创建新记录）。
            请求体中可以包含大量数据。
            不会被缓存。
        PUT
        用途：用于更新已有的资源或创建新的资源。
        特点：
            请求体包含更新后的完整资源。
            如果资源不存在，PUT方法通常会创建它。
        DELETE
        用途：用于删除指定的资源。
        特点：
            通过请求行中的URL指定要删除的资源。
        PATCH
        用途：用于部分更新已有的资源。
        特点：
            只提交需要更改的部分，而不是整个资源。
            请求体中包含要修改的字段及其新值。
        OPTIONS
        用途：用于询问服务器支持的HTTP方法和其他选项。
        特点：
            服务器可以返回支持的请求方法列表。
        HEAD
        用途：类似于GET，但只请求响应头，不返回响应体。
        特点：
            常用于检查资源的状态或获取元数据。
        可以包含请求体的方法：POST、PUT、PATCH、DELETE（不常用）
    请求头：
        Host：指定请求的服务器地址，如www.example.com。
        Content-Type：指定请求体的数据类型，如application/json。
        Authorization：指定请求的身份验证信息，如Bearer <token>。
        User-Agent：指定客户端的浏览器类型和版本，如Mozilla/5.0。
        Accept：指定客户端可以接收的数据类型，如application/json。
        Accept-Language：指定客户端可以接收的语言，如en-US。
        Accept-Encoding：指定客户端可以接收的编码格式，如gzip。
        Cookie：指定客户端的cookie信息，如sessionid=123456。
    请求参数：
        查询参数：附加在URL末尾的参数，以?开始，多个参数用&分隔，参数均为键值对形式。
            用途：用于传递额外的信息，如过滤、排序或搜索条件。
            示例：GET /search?query=apple&sort=asc
            常用请求方法：GET、DELETE
        路径参数：嵌入在URL路径中的参数，用于标识特定的资源。
            用途：通常用于动态访问资源，如用户、产品等。
            示例：GET /users/100001
            常用请求方法：GET、DELETE、PUT
        请求体参数：包含在HTTP请求体中的数据，通常用于提交复杂数据结构。
            用途：用于传递创建或更新资源所需的数据，尤其是当数据量较大时。
            示例（JSON格式）：
                {
                    "username": "john",
                    "password": "12345"
            }
            常用请求方法：POST、PUT、PATCH
    请求体：
        请求体包含了实际要发送给服务器的数据，通常在POST、PUT和PATCH请求中使用。请求体的内容可以是多种格式，包括：
        表单数据：通常用于提交HTML表单数据，格式为``application/x-www-form-urlencoded``或``multipart/form-data``。
            示例：username=john&password=12345
        JSON数据：通常用于提交复杂数据结构，格式为``application/json``。
            示例：{"username": "john", "password": "12345"}
        XML数据：通常用于提交复杂数据结构，格式为``application/xml``。
            示例：
                <user>
                    <username>john</username>
                    <password>12345</password>
                </user>
        文件上传：通常用于上传文件，格式为``multipart/form-data``。
            示例：上传文件的表单数据
    HTTP响应结构与请求结构类似，都是由状态行、响应头和响应体组成。响应包含状态信息、附加信息和实际的数据，以便客户端理解请求的结果。
    状态行包含HTTP版本、状态码和状态描述。比如：HTTP/1.1 200 OK
    常见状态码：
        1xx：信息性状态码，表示请求已被接收，继续处理。例：
            100 Continue：初始请求已接受，客户端可以继续发送请求体
            101 Switching Protocols：服务器已理解客户端请求，正在切换协议
        2xx：成功状态码，表示请求已成功被服务器接收、理解和接受。例：
            200 OK：请求成功，服务器返回请求的资源。
            201 Created：请求成功，资源已被创建（通常用于POST请求）。
            204 No Content：请求成功，但没有返回任何内容。
        3xx：重定向状态码，表示需要客户端采取进一步的操作才能完成请求。例：
            301 Moved Permanently：请求的资源已被永久移动到新位置，通常伴随新的URL。
            302 Found：请求的资源临时移动到新位置，客户端应继续使用原始URL。
            304 Not Modified：客户端的缓存版本仍然有效，服务器没有返回新的内容。
        4xx：客户端错误状态码，表示请求包含错误语法或无法被服务器理解。例：
            400 Bad Request：请求有误，服务器无法理解。
            401 Unauthorized：请求需要身份验证，未提供有效凭证。
            403 Forbidden：服务器拒绝请求，客户端没有权限访问资源。
            404 Not Found：请求的资源未找到。
        5xx：服务器错误状态码，表示服务器在处理请求时发生了错误。例：
            500 Internal Server Error：服务器遇到意外情况，无法完成请求。
            502 Bad Gateway：服务器作为网关或代理时，收到无效响应。
            503 Service Unavailable：服务器暂时无法处理请求，通常由于过载或维护。
            
3. request库
    Python 爬虫的核心是模拟浏览器向网站发送请求，并从返回的网页中提取所需的数据。
    request库是一个用于发送HTTP请求的Python库，它提供了简单易用的API来处理各种HTTP请求，包括GET、POST、PUT、DELETE等。
    请求方法的使用：
        1. 发送GET请求：
            ``response = requests.get('https://www.example.com')``
            注：GET请求可以带有查询参数，比如
            ``response = requests.get('https://www.example.com', params={'name': 'Alice', 'age': 30})``
        2. 发送POST请求：
            ``data = {'username': 'user123', 'password': 'pass123'}``
            ``response = requests.post('https://www.example.com/login', data=data)``
        3. 发送PUT请求：
            ``data = {'name': 'Alice', 'age': 30}``
            ``response = requests.put('https://www.example.com/users/123', json=data)``
        4. 发送DELETE请求：
            ``response = requests.delete('https://www.example.com/users/123')``
    请求头的使用：
        请求头用于传递一些额外信息，比如客户端信息、授权信息、内容类型等。
        在requests中，可以通过 headers 参数传递自定义请求头：
            ``headers = {``
                ``'User-Agent': 'Mozilla/5.0',``
                ``'Authorization': 'Bearer token123'``
                ``'Content-Type': 'application/json'``
                ``'Accept': 'text/html'``
            ``}``
    请求体的使用：
        请求体主要用于POST、PUT和PATCH请求，用于传递数据给服务器。
        表单数据：
            使用 data 参数传递表单数据，格式为字典或元组列表
                ``data = {'key1': 'value1', 'key2': 'value2'}``
                ``response = requests.post('https://www.example.com/form', data=data)``
        JSON数据：
            使用 json 参数，格式为字典，requests会自动将数据转换为JSON格式
                ``json_data = {'name': 'Alice', 'age': 30}``
                ``response = requests.post('https://www.example.com/api', json=json_data)``
        XML数据：
            使用 data 参数，格式为文档字符串需要手动设置请求头中的 Content-Type 为 application/xml
                ``xml_data = example``
                ``headers = {'Content-Type': 'application/xml'}``
                ``response = requests.post('https://www.example.com/api', data=xml_data, headers=headers)``
        文件上传：
            使用 files 参数，格式为字典，其中键是字段名，值是文件对象
                ``files = {'file': open('example.txt', 'rb')}``
                ``response = requests.post('https://www.example.com/upload', files=files)``
                注：上传文件时，需要将文件对象设置为二进制模式（'rb'）；如有需要，可以将Content-Type设置为 multipart/form-data
    响应处理：
        1. 通过响应状态码判断请求是否成功：
            ``if response.status_code == 200:``
        2. 获取响应头：
            ``headers = response.headers``
        3. 获取响应体：
            获取HTML内容：返回网页的HTML内容
                ``html_content = response.text``
            获取JSON内容：返回JSON格式的数据，前提是服务器返回的是JSON格式的数据
                ``url = 'https://jsonplaceholder.typicode.com/todos/1'``
                ``response = requests.get(url)``
                ``json_content = response.json()``
                注：如果访问的是网页的API，且服务器返回的是JSON格式的数据，可以使用response.json()方法解析
            获取二进制内容：返回原始的二进制数据，适用于下载文件或图片
                ``url = 'https://www.example.com/image.jpg'``
                ``response = requests.get(url)``
                ``binary_content = response.content``
                注：对于图片、音频等二进制数据，可以使用 response.content 获取

4. BeautifulSoup库
    BeautifulSoup 是一个用于解析HTML和XML文档的Python库，它可以将HTML或XML文档解析为一个树形结构，方便我们提取其中的数据。
    使用方法：
        1. 导入库并创建对象：
            ``from bs4 import BeautifulSoup``
            ``soup = BeautifulSoup(html_content, 'html.parser')``
            html.parser 是一个 Python 内置的解析器，适用于简单的 HTML 文档解析，优点是轻便易用，但性能和功能有限。
            lxml 解析器更快，既可以处理 HTML 也可以处理 XML ，适合处理复杂结构或需要高性能的应用，但需要额外安装。
        2. 提取数据：
            查询元素：
                1. 标签查找： find(), find_all()
                    ``soup.find('tag_name')``
                    ``soup.find_all('tag_name')``
                    注： find() 返回第一个匹配的元素， find_all() 返回所有匹配的元素，返回值是列表。
                2. 属性查找： find(), find_all()与属性值
                    ``soup.find('tag_name', class='content')``
                    ``soup.find_all('tag_name', id='first')``
                    注： class 和 id 是 HTML 元素的属性，可以根据属性值查找元素。
                3. 结合多个条件查找： find()与字典
                    ``soup.find('tag_name', {'attr1': 'value1', 'attr2': 'value2'})``
                    注：可以通过字典的形式指定多个属性值，查找满足所有条件的元素。
                4. CSS 选择器： select()
                    ``soup.select('tag_name.class_name')``
                    ``soup.select('tag_name#id_name')``
                5. 文本查找： find()与text属性
                    ``soup.find('tag_name', text='text_content')``
                    注： text属性可以用于查找包含特定文本的元素。
                6. 正则表达式： find()与re模块
                    ``import re``
                    ``soup.find('tag_name', text=re.compile('pattern'))``
                    注：正则表达式可以用来处理动态页面结构、处理文本的变体以及筛选复杂的 HTML 结构
                7. 导航文档树：
                    父节点：.parent
                        ``soup.find('tag_name').parent``
                    子节点：.children
                        ``for child in soup.find('tag_name').children:``
                        ``    print(child)``
                    兄弟节点：.next_sibling, .previous_sibling
                        ``soup.find('tag_name').next_sibling``
                        ``soup.find('tag_name').previous_sibling``
            提取属性：
                在使用 BeautifulSoup 查找 HTML 标签后，得到的标签对象实际上是一个 Tag 对象，通过 Tag 对象，我们需要通过特定的方式来提取我们需要的内容，比如属性或内部文本。
                例： ``<a href="https://www.example.com">Example</a>``
                    ``tag = soup.find('a')``
                提取属性：
                    使用 tag['attribute_name'] 或 tag.get('attribute_name') 来获取特定属性的值
                        ``href_value = tag['href']``
                        ``href_value = tag.get('href')``
                    注：如果属性不存在， tag['attribute_name'] 会抛出 KeyError 异常，而 tag.get('attribute_name') 会返回 None。
                提取文本：
                    使用 .text 或 .get_text() 方法可以获取标签内部的文本内容。
                        ``text_content = tag.text``
                        ``text_content = tag.get_text()``
                    注：.text 是一种简便的方式直接获取文本，而.get_text() 提供了更多灵活性和控制，比如你可以自定义分隔符和是否去除空白字符。
                    .get_text() 方法的参数列表：
                        separator ：定义文本之间的分隔符。
                        strip ：如果设置为 True ，会去除首尾的空白字符。
                        
5. 反爬虫机制
    很多网站为了防止自动化脚本（如爬虫）大量抓取数据，都会采用反爬虫机制。为了应对这些机制，我们需要采取一些措施来模拟人类浏览器的行为，以避免被网站封禁。
    1. IP 限制：网站可以通过监控短时间内某个 IP 发出的请求频率来判断是否为爬虫，如果请求频率过高，服务器会暂时或永久封禁该 IP 地址，导致请求失败。
        解决方法：
        1. 代理IP ：通过代理池使用多个不同的 IP 地址轮流发送请求，避免频繁使用同一 IP。
            ``proxies = {``
                            ``"http": "http://your_proxy_ip:your_proxy_port",``
                            ``"https": "https://your_proxy_ip:your_proxy_port"``
            ``          }``
            ``url = "https://example.com"``
            ``response = requests.get(url, proxies=proxies)``
            ``print(response.text)``
            如何获取代理IP：可以从一些免费代理网站获取代理 IP ，也可以通过付费服务提供的代理池。推荐 GitHub 项目： ProxyPool
        2. 延时请求：在每次发送请求后，程序会暂停一段时间再继续发送下一个请求，目的是模拟正常用户的行为，避免频繁请求导致 IP 被封。可以通过 time.sleep() 函数实现延时。
            ``import time``
            ``for _ in range(5):``
                ``response = requests.get(url)``
                ``print(response.status_code)``
                ``delay = random.uniform(1, 5)``
                ``time.sleep(delay)``
        可以结合这两种方法，每次请求都会随机选择一个代理 IP ，并在发送请求后加入随机延时，这样能够有效地降低被检测和封禁的可能性。
        ``proxies = {``
                    ``"http": "http://your_proxy_ip:your_proxy_port",``
                    ``"https": "https://your_proxy_ip:your_proxy_port"``
        ``      }``
        ``for _ in range(5):``
            ``proxy = random.choice(proxies)``
            ``response = requests.get(url, proxies=proxy)``
            ``print(response.status_code)``
            ``delay = random.uniform(1, 5)``
            ``time.sleep(delay)``
    2. User-Agent 检测： User-Agent 是 HTTP 请求头中的一个字段，它告诉服务器客户端的类型和版本。对于普通用户来说， User-Agent 通常标识了他们所使用的浏览器和操作系统。
        如果没有指定 User-Agent ，或 User-Agent 是默认的爬虫标识（如 Python-requests ），网站可能会拒绝响应。因此，在爬虫中设置合适的 User-Agent 是绕过这类反爬虫机制的常见方式。
        解决方法：
        1. 在请求头中添加 User-Agent 字段：可以通过传递自定义的请求头来修改 User-Agent。这可以在发送请求时加入 headers 参数来实现。
            ``headers = {``
                ``"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"``
            ``}``
            ``url = "https://example.com"``
            ``response = requests.get(url, headers=headers)``
            ``print(response.status_code)``
        2. 动态变换 User-Agent ： 为了进一步避免检测，可以在每次请求时随机变换 User-Agent，这样服务器不会因为每次请求都带有相同的 User-Agent 而怀疑是爬虫。
            ``import random``
            ``user_agents = [``
                            ``"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",``
                            ``"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15",``
                            ``"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko"``
                    ``]``
            ``url = "https://example.com"``
            ``headers = {``
                        ``"User-Agent": random.choice(user_agents)``
                  ``}``
            ``response = requests.get(url, headers=headers)``
            ``print(f"Status Code: {response.status_code}, User-Agent: {headers['User-Agent']}")``
    3. Cookie 和 Session 检测：在 Web 应用中，通常会在用户登录时创建 Session ，并在 Session 中存储用户的信息。同时，服务器会在响应中发送一个 Cookie ，包含 Session ID ，用于客户端识别和访问该 Session。如果爬虫没有正确处理 Cookie 和 Session ，服务器可能会拒绝响应。
        判断访问是否被拒绝：
            浏览器中打开网页，查看开发者工具中的 Network 标签页，找到对应的请求文件（ xhr 后缀），查看请求与响应的各参数。
            1. 检查响应状态码：如果服务器返回的状态码是 401 （未授权）、 403 （禁止访问）或 302 （重定向到登陆页面），则表示访问被拒绝。
            2. 检查响应头与请求头：查看响应头中的 Set-Cookie 字段，以及请求头中的 Cookie 字段。如果响应头中包含 Set-Cookie 字段，则服务器希望客户端在后续请求中携带该 Cookie 。如果请求头中缺少 Cookie 字段，则服务器可能拒绝响应。除此之外， Authorization 字段也用于 Token 认证，可能包含认证信息。
            3. 检查响应内容：如果响应内容中包含提示信息，如“请先登录”、“需要登录才能访问”等，则表示访问被拒绝。
        解决方法：
        1. 使用 requests 库里的 Session 对象：创建一个 POST 请求，将用户名和密码以表单数据的形式发送给服务器，服务器会返回一个包含 Session ID 的 Cookie 。
            ``import requests``
            ``login_url = "https://example.com/login"``
            ``login_data = {``
                            ``"username": "your_username"``
                            ``"password": "your_password"``
                        ``}``
            ``session = requests.Session()``
            ``response = session.post(login_url, data=login_data)``
            ``print(response.status_code)``
            通过 Session 对象，可以保持会话状态，并在后续请求中自动携带 Cookie 。
            ``url = "https://example.com/protected"``
            ``response = session.get(url)``
            ``print(response.status_code)``
        2. 手动获取 Cookie 并添加到请求头：如果无法使用 Session 对象，可以手动从浏览器中复制 Cookie ，并添加到请求头中。
            ``import requests``
            ``url = "https://example.com"``
            ``cookies = {``
                ``'sessionid': 'your-session-cookie-value',``
                ``'csrftoken': 'your-csrf-token',  ``
            ``}``
            ``response = requests.get(url, cookies=cookies)``
            ``print(response.text)``
        3. 使用浏览器自动化工具：如 Selenium ，可以模拟浏览器行为，自动处理 Cookie 和 Session 。
            ``from selenium import webdriver``
            ``driver = webdriver.Chrome()``
            ``driver.get("https://example.com/")``
            ``cookies = driver.get_cookies()``
            ``driver.quit()``
    4. JavaScript 动态加载：许多现代 Web 应用使用 JavaScript 动态生成页面内容，而不是直接从服务器获取。在这种情况下，使用 requests 库无法获取到完整的页面内容，因为 requests 库无法执行 JavaScript 代码。
        解决方法：
        1. 使用网站的 API ：如果网站提供了 API ，可以直接使用 API 获取数据，而不需要使用爬虫。
            ``import requests``
            ``api_url = "https://example.com/api/data"``
            ``response = requests.get(api_url)``
            如何查找 API ：
                1. 打开开发者工具，切换到 Network 标签页。
                2. 筛选网络请求：在请求类型里，你可能会看到 XHR、Fetch、JS、Doc 等不同的文件类型。API 请求通常以 XHR 或 Fetch 为主，这两个类型通常表示动态数据请求，通常就是通过 API 来获取数据的。可以点击它们，查看请求的 URL 和响应数据。
                3. 分析 API 请求：
                    URL ： API 请求的 URL 通常比较简洁，并且带有像 /api/、/v1/、/products/、/users/ 等路径，表明是一个数据接口。
                    请求方法：常见的 API 请求会使用 GET 或 POST 方法。
                    响应数据：如果响应的数据是 JSON、XML 这样的结构化数据，而不是 HTML 页面内容，那么可以确定这是一个 API 请求。
        2. 使用浏览器自动化工具：当网页的内容完全由 JavaScript 渲染，无法通过 API 抓取时，可以使用 Selenium 等浏览器自动化工具来模拟用户操作，加载整个页面并获取数据。
            ``from selenium import webdriver``
            ``from selenium.webdriver.common.by import By``
            ``driver.get("https://example.com")``
            ``driver.implicitly_wait(10)``
            ``element = driver.find_element(By.ID, "content")``
            ``driver.quit()``
            也可以使用更轻量级的工具 requests-html ，或是使用 Pyppeteer 等工具来处理 JavaScript 渲染的页面。
        3. 使用 API 提供的抓取服务：一些 API 提供商可能会提供一些抓取服务，比如爬虫代理、 API 调用次数限制等，可以尝试联系 API 提供商获取帮助。
            ``import requests``
            ``api_key = 'your-api-key'``
            ``url = 'https://example.com'``
            ``response = requests.get(f'http://api.scraperapi.com/?api_key={api_key}&url={url}')``
            ``print(response.text)``
    5. 验证码：验证码（ CAPTCHA ）是网站用来验证访问者是否为人类的常见防爬虫机制。验证码的主要目的是防止自动化脚本绕过网站的验证，因此应对验证码是一个复杂的过程，很多时候需要结合不同的技术和策略。
        解决方法：
        1. 手动输入：最简单的方式是将爬虫暂停，手动解决验证码，然后继续爬虫。这种方法适用于验证码比较简单，且不需要频繁输入的情况。
            ``import time``
            ``time.sleep(60)``
        2. 使用第三方服务：有一些第三方服务提供验证码识别服务，比如 2Captcha 、 Anti-Captcha 等。使用这些服务，可以处理一些图片验证码。
            ``import requests``
            ``api_key = 'your-api-key'``
            ``with open('captcha_image.png', 'rb') as captcha_file:``
                ``files = {'file': captcha_file}``
                ``response = requests.post(f'http://2captcha.com/in.php?key={api_key}&method=post', files=files)``
            ``captcha_id = response.text.split('|')[1]``
            ``time.sleep(60)``
            ``response = requests.get(f'http://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}')``
            ``captcha_solution = response.text.split('|')[1]``
        3. 使用 Selenium 处理滑动验证码：有些验证码是滑动验证码，可以使用 Selenium 模拟用户操作来解决。
            ``from selenium import webdriver``
            ``from selenium.webdriver.common.action_chains import ActionChains``
            ``driver = webdriver.Chrome()``
            ``driver.get("https://example.com")``
            ``slider = driver.find_element(By.ID, "slider")``
            ``actions = ActionChains(driver)``
            ``actions.click_and_hold(slider).perform()``
            ``actions.move_by_offset(200, 0).perform()``
            ``actions.release().perform()``
            ``driver.quit()``
        4. 使用机器学习模型：对于一些复杂的验证码，可以使用机器学习模型来识别。这通常需要大量的训练数据，并且需要一定的机器学习知识。
    

6. Matplotlib 库： Matplotlib 是一个用于创建静态、动态和交互式可视化的 Python 库。它提供了丰富的绘图功能，可以绘制各种类型的图表。
    Matplotlib 可绘制的图表：折线图、散点图、柱状图、饼图、直方图、箱线图、误差条形图与热图等。
    1. 图表绘制的基本元素：
        ① 图表标题：使用 plt.title() 添加图表标题。
            ``plt.title("Chart Title", fontsize=16, color='red')``
                ``label`` ：图表标题的文本，字符串类型。
                ``fontsize`` ：设置字体大小，数值或 small, medium, large 等字符串。
                ``color`` ：设置字体颜色，接受标准的颜色名称（如 'red', 'blue'）或者十六进制颜色代码（如 #00FF00 ）。
                ``loc`` ：标题的对齐方式。默认为 'center'，也可以是 'left' 或 'right'。
                ``pad`` ：标题与图表之间的距离，单位为点（ points ），默认为 6.0 。
        ② 图例：使用 plt.legend() 添加图例。
            ``plt.legend(loc='upper right', fontsize=10, title='图例')``
                ``loc`` ：图例的位置，可以是 'best'、'upper right'、'lower left' 等等。也可以用数字 0-10 来指定位置， 0 表示 'best' ， 1 表示 'upper right'，以此类推。
                ``fontsize`` ：图例字体大小，可以是数字形式，也可以是 'xx-small'、'x-small'、'small'、'medium'、'large'、'x-large'、'xx-large' 等等。
                ``title`` ：图例标题。
        ③ X 轴或 Y 轴标签：使用 plt.xlabel() 或 plt.ylabel() 添加 X 轴或 Y 轴标签。
            ``plt.xlabel("X Axis Label", fontsize=12, color='blue')``
                ``label`` ：轴标签的文本，字符串类型。
                ``fontsize``：设置字体大小，数值或 small, medium, large 等字符串。
                ``color``：设置字体颜色，接受标准的颜色名称（如 'red', 'blue'）或者十六进制颜色代码（如 #00FF00 ）。
                ``loc``：标签的对齐方式，'left' / 'right' 对于 x 轴标签， 'top' / 'bottom' 对于 y 轴标签。
        ④ X 轴或 Y 轴取值范围：使用 plt.xlim() 或 plt.ylim() 设置 X 轴或 Y 轴的取值范围。
            ``plt.xlim(min_value, max_value)``
            ``plt.ylim(min_value, max_value)``
        ⑤ 网格线：使用 plt.grid() 添加网格线。
            ``plt.grid(True, which='both', color='gray', linestyle='--', linewidth=0.5)``
                ``b`` ：布尔值，是否显示网格线。
                ``which`` ：控制网格线的显示类型，'major'显示主刻度的网格线（默认），'minor'显示次刻度的网格线，'both'显示所有网格线。
                ``color`` ：设置网格线的颜色，接受标准的颜色名称（如 'red', 'blue'）或者十六进制颜色代码（如 #00FF00 ）。
                ``linestyle`` ：设置网格线的样式，可以是 '-'（实线）、'--'（虚线）、'-.'（点划线）、':'（虚线）等。
                ``linewidth`` ：设置网格线的宽度。
        ⑥ 图形大小：使用 plt.figure(figsize=(width, height)) 设置图形大小。
            ``plt.figure(figsize=(10, 6))``
                ``figsize`` ：图形的尺寸，以英寸为单位，宽度和高度。
                ``width`` ：图形的宽度，单位为英寸。
                ``height`` ：图形的高度，单位为英寸。
    2. 图表输出：使用 plt.savefig() 保存图表。
        ``plt.savefig('filename.png', dpi=300, bbox_inches='tight')``
            ``filename`` ：保存的文件名，可以是相对路径或绝对路径。
            ``dpi`` ：分辨率，默认为 300。
            ``bbox_inches`` ：图表边框，'tight' 表示紧凑，'normal' 表示正常，'loose' 表示宽松。
    3. 各类图表的绘制方法：
        1. 折线图：折线图是最基础的图表类型，用于展示数据的连续变化。
            函数：``plt.plot()``
            示例：``plt.plot(x, y, linestyle='-', marker='o', color='b', linewidth=2)``
            参数列表：
                x: x 轴的数据，列表或数组。
                y: y 轴的数据，列表或数组。
                color: 线条的颜色，可以是颜色名称（'blue'、'red'）或者 RGB 十六进制值（如 '#00FF00'）。
                linestyle: 线条样式，常见选项有：'-': 实线（默认）、'--': 虚线、'-.': 点划线、':': 虚线。
                marker: 设置数据点的标记样式，常见选项包括：'o': 圆点、's': 方形、'^': 上三角、'v': 下三角、'x': 叉号、'D': 菱形、'p': 五边形、'*': 星号等。
                linewidth: 线条宽度，默认为 1.5。
        2. 柱状图：柱状图用于比较不同类别的数据。
            函数：``plt.bar()``
            示例：``plt.bar(x, height, width=0.8, color='blue', edgecolor='black')``
            参数列表：
                x: x 轴的类别或位置，列表或数组。
                height: 每个柱状条的高度。
                width: 每个柱状条的宽度，默认为 0.8。
                color: 柱状条的颜色，可以是颜色名称（'blue'、'red'）或者 RGB 十六进制值（如 '#00FF00'）。
                edgecolor: 柱状条边缘的颜色，默认为 'black'。
        3. 散点图：散点图用于显示两组数据的相关性或分布情况。
            函数：``plt.scatter()``
            示例：``plt.scatter(x, y, s=area, c=colors, alpha=0.5)``
            参数列表：
                x: x 轴的数据，列表或数组。
                y: y 轴的数据，列表或数组。
                s: 散点的大小，默认为 20 ，可以传入列表。
                c: 散点的颜色，可以是单一颜色或颜色列表。
                alpha: 透明度，取值范围 0 （完全透明）到 1 （完全不透明）。
        4. 饼图：饼图用于展示不同类别的比例。
            函数：``plt.pie()``
            示例：``plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, explode=explode)``
            参数列表：
                sizes: 每个扇区的数据，列表或数组。
                labels: 每个扇区的标签，列表或数组。
                colors: 每个扇区的颜色，列表或数组。
                autopct: 用于显示每个部分的百分比，格式如 '%1.1f%%'。
                startangle: 饼图的起始角度，默认从 0 开始，可以通过设置 90 来使第一个部分从正上方开始。
                explode: 控制某个部分与其他部分的距离，通常用于突出某一部分。
        5. 箱线图：箱线图用于显示数据的分布情况，尤其是数据的中位数、四分位数和异常值。
            函数：``plt.boxplot()``
            示例：``plt.boxplot(data, patch_artist=True, boxprops=dict(facecolor='lightblue'))``
            参数列表：
                data: 数据，可以是列表或二维数组。
                patch_artist: 是否填充箱线图，默认为 False。
                boxprops: 设置箱子属性， dict(facecolor='lightblue') 用于设置箱子的颜色。
        6. 直方图：直方图用于展示数据的分布情况，常用于显示频率分布。
            函数：``plt.hist()``
            示例：``plt.hist(data, bins=10, color='blue', edgecolor='black', alpha=0.7)``
            参数列表：
                data: 数据，列表或数组。
                bins: 指定直方图的柱状条数，默认是 10。
                color: 柱状条颜色。
                edgecolor: 柱状条的边框颜色。
                alpha: 柱状条的透明度，取值范围 0-1。
        7. 误差棒图：误差棒图用于显示数据点的误差范围。
            函数：``plt.errorbar()``
            示例：``plt.errorbar(x, y, yerr=errors, fmt='o', ecolor='red', capsize=5)``
            参数列表：
                x: x 轴的数据，列表或数组。
                y: y 轴的数据，列表或数组。
                yerr: y 轴方向的误差值，可以是列表或单一数值。
                xerr: x 轴方向的误差值，可以是列表或单一数值。
                fmt: 数据点的标记样式，类似于 plt.plot() 中的 marker 参数。
                ecolor: 误差棒的颜色。
                capsize: 设置误差棒的末端横线长度。
        8. 热力图：热力图用于展示数据矩阵的分布情况。
            函数：``plt.imshow()``
            示例：``plt.imshow(data, cmap='hot', interpolation='nearest')``
            参数列表：
                data: 数据矩阵，二维数组。
                cmap: 颜色映射，常见选项包括：'hot': 热色、'cool': 冷色、'viridis': 绿色到紫色的渐变等。默认为 'viridis'。
                interpolation: 插值方法，常见选项包括：'nearest': 最近邻插值、'bilinear': 双线性插值、'bicubic': 双三次插值等。默认为 'nearest'。
        9. 3D 图： 3D 图用于展示三维数据。
            函数：``ax.plot_surface()``
            示例：``ax.plot_surface(X, Y, Z, cmap='viridis')``
            参数列表：
                X, Y, Z: 三维坐标数据，通常是二维数组。
                cmap: 颜色映射，常见选项包括：'viridis': 绿色到紫色的渐变、'plasma': 红色到紫色的渐变、'inferno': 红色到黄色的渐变、'magma': 红色到黑色的渐变、'cividis': 蓝色到黄色的渐变等。默认为 'viridis'。
        10. 子图：子图用于在一个图中绘制多个子图。
            函数：``plt.subplots()``
            示例：``fig, axs = plt.subplots(2, 2)``
            参数列表：
                nrows: 子图的行数。
                ncols: 子图的列数。
                sharex: 是否共享 x 轴，默认为 False。
                sharey: 是否共享 y 轴，默认为 False。

"""

import requests
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
import numpy as np

# 使用 requests 获取数据
url = 'https://www.tiobe.com/tiobe-index/'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    'Host': 'www.tiobe.com',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}

response = requests.get(url, headers=header)
# 检测连接是否正常
if response.status_code == 200:
    print('连接成功')
else:
    print(f'连接失败，状态码为：{response.status_code}')
    
# 使用 BeautifulSoup 解析数据
soup = bs(response.text, 'html.parser')

# 获取表格数据
table = soup.find('table', {'id': 'VLTH', 'class': 'table table-striped'})

years = [year.text for year in table.find_all('th')[:0:-1]]
languages = []
rankings = []
for tr in table.find_all('tr')[1:]:
    cols = tr.find_all('td')
    if all(x not in cols[0].text for x in ['Visual Basic', '(Visual) Basic', 'SQL']):
        languages.append(cols[0].text)
        ranks = [int(col.text) if col.text.isdigit() else None for col in cols[:0:-1]]
        rankings.append(ranks)
    else:
        continue

rank_array = np.array(rankings, dtype=float)

# 绘制折线图
plt.figure(figsize=(10, 6))
marker = ['o', 'v', '^', '<', '>', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd']
for i, language in enumerate(languages):
    plt.plot(years, rank_array[i], label=language, marker=marker[i])
    
# 添加图例、标题和标签
plt.legend(loc = 'upper left', ncol=2)
plt.xlabel('Year')
plt.ylabel('Ranking')
plt.title('Programming Language Ranking in 1989-2024')

# 展示图形并保存
plt.savefig('ex_figure/Ex11_数据可视化.png', dpi=500)
plt.show()