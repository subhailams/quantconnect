class FormalFluorescentYellowArmadillo(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 1, 1)  # Set Start Date
        self.SetEndDate(2021, 1, 1) # Set End Date
        self.SetCash(100000)  # Set Strategy Cash
        
        goog = self.AddEquity("GOOG", Resolution.Daily)
        # self.AddForex, self.AddFuture...
        goog.SetDataNormalizationMode(DataNormalizationMode.Raw)
        self.goog = goog.Symbol 
        
        appl = self.AddEquity("APPL", Resolution.Daily)
        appl.SetDataNormalizationMode(DataNormalizationMode.Raw)
        self.appl = appl.Symbol 
        
        self.SetBenchmark("GOOG")
        self.SetBrokerageModel(BrokerageName.InteractiveBrokersBrokerage, AccountType.Margin)
        
        self.entryPrice = 0
        
        self.day = 0
        self.price_0 = 0
        self.price_5 = 0
        
        self.prices = []
        
        # self.period = timedelta(31)
        # self.nextEntryTime = self.Time

    def OnData(self, data):
        if not self.goog and self.appl in data:
            return
        
        price = data[self.goog].Close
        self.prices.append(price)
        
        if len(self.prices) > 20:
            for i in range(5,20):
                curr = self.prices[i] 
                past = self.prices[i-5]
                aplha1 = -1 * ((curr - past) / past)
                self.Log("Alpha1: " + str(aplha1))
        
        # if self.day == 0: # First day
        #     self.price_0 = data[self.goog].Close
            
        
        # elif self.day % 5 == 0:
        #     self.price_5 = data[self.goog].Close
            
        #     self.Log(str(self.day) + ":" + str(self.price_0) + "," + str(self.price_5))
        #     self.price_0 = self.price_5
            
        
        # self.day += 1
    
        
        # if not self.Portfolio.Invested:
            
        #     last_price =data[self.goog][-6].Close
            
        #     if price < last_price:
        #         self.SetHoldings([PortfolioTarget("GOOG", 1), PortfolioTarget("APPL", -0.5)])
        #         self.Log("BUY GOOG @" + str(price))
        #     else:
        #         self.SetHoldings([PortfolioTarget("GOOG", -1), PortfolioTarget("APPL", 0.5)])
        #         self.Log("SELL GOOG @" + str(price))               
            
        #     if self.nextEntryTime <= self.Time:
        #         self.SetHoldings(self.spy, 1)
        #         # self.MarketOrder(self.spy, int(self.Portfolio.Cash / price) )
        #         self.Log("BUY SPY @" + str(price))
        #         self.entryPrice = price
        
        # elif self.entryPrice * 1.1 < price or self.entryPrice * 0.90 > price:
        #     self.Liquidate()
        #     self.Log("SELL SPY @" + str(price))
        #     self.nextEntryTime = self.Time + self.period
