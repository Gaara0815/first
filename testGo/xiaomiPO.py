#首页
class IndexPage():
    def __init__(self,driver):
        self.driver=driver
        # 访问小米页面-确保操作的时候处于首页
        self.driver.get('https://www.mi.com/')

    #进入登录页
    def to_login(self):
        # 登录-点击登录按钮
        self.driver.find_element_by_css_selector('#J_siteUserInfo>a:nth-child(1)').click()
        # 处理用户协议
        btns = self.driver.find_elements_by_class_name('btn-primary')
        # 假如出现用户协议弹出按钮
        if btns:
            btns[0].click()

        #返回登录页对象
        return LoginPage(self.driver)

    #搜索商品
    def search_item(self,item='小米10 Pro'):
        # 搜索商品
        self.driver.find_element_by_id('search').send_keys(item+'\n')
        return GoodItemsPage(self.driver)

#登录页
class LoginPage():
    def __init__(self, driver):
        self.driver = driver
    #账号密码登录
    def login(self,username,psw):
        # 输入用户名密码
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('pwd').send_keys(psw)
        # 点击登录
        self.driver.execute_script("document.getElementById('login-button').click()")
        #返回首页对象
        return IndexPage(self.driver)

#商品页面
class GoodItemsPage():
    def __init__(self, driver):
        self.driver = driver

    #选择商品
    def pick_item(self):
        # 选择第一个结果
        self.driver.find_element_by_css_selector('#J_goodsList>div:nth-child(1) a').click()

        # 切换到商品详情页窗口
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            # 判断切换到目标窗口-判断当前窗口标题是否为：小米10系列立即购买-小米商城
            if '小米10系列立即购买-小米商城' == self.driver.title:
                print('切换到目标窗口')
                #进入到商品详情页
                return ItemPage(self.driver)

#商品详情页
class ItemPage():
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        # 点击加入购物车
        self.driver.find_element_by_css_selector('.sale-btn>a').click()
        return ShopCartPage(self.driver)

#购物车页面
class ShopCartPage():
    def __init__(self, driver):
        self.driver = driver

    def check_item(self):
        # 检查是否添加成功
        res = self.driver.find_element_by_class_name('goods-info').text
        assert '小米10 全网通版' in res
        #如果操作涉及页面跳转-需要返回对应的页面对象，如果没有则不需要返回


if __name__ == '__main__':
    #首页-进入登录-登录-首页-搜索商品-商品页面-选择商品-进入商品详情页-添加购物车-购物车页面-检查是否添加成功
    from selenium import webdriver
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)

    indexpage=IndexPage(driver)

    loginPage=indexpage.to_login()

    indexpage=loginPage.login('你的账号','你的密码')

    goodItemsPage=indexpage.search_item()

    itemPage=goodItemsPage.pick_item()

    shopCartPage=itemPage.add_to_cart()

    shopCartPage.check_item()

    driver.quit()
