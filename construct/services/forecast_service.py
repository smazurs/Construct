class ForecastService:
    @staticmethod
    def forecast_project_cost(material_cost, labor_cost, equipment_cost, growth_rate=0.05, years=1):
        """
        Forecasts future project costs based on an annual growth rate.
        
        :param material_cost: Current material cost
        :param labor_cost: Current labor cost
        :param equipment_cost: Current equipment cost
        :param growth_rate: Expected annual growth rate (default 5%)
        :param years: Number of years to forecast (default 1 year)
        :return: Forecasted total cost after specified years
        """
        total_cost = material_cost + labor_cost + equipment_cost
        forecasted_cost = total_cost * ((1 + growth_rate) ** years)
        return forecasted_cost
