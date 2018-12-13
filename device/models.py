from django.db import models



class Vender(models.Model):

    name = models.CharField(verbose_name='供应商名称', max_length=200)
    address = models.CharField(verbose_name='地址', max_length=200)
    email = models.EmailField(verbose_name='电子邮件' )
    phone = models.CharField(verbose_name='电话', max_length=20)

    class Meta:
        verbose_name = '供应商'
        verbose_name_plural = '供应商'

    def __str__(self):
        return self.name


class Category(models.Model):

    name = models.CharField(verbose_name='种类名称', max_length=100)
    rank = models.CharField(max_length=120, blank=True)
    
    class Meta:
        verbose_name='设备种类'
        verbose_name_plural = '设备种类'
    
    def __str__(self):
        return self.name



class Device(models.Model):

    number = models.CharField(verbose_name='设备编号', max_length=100)
    category = models.ForeignKey(Category, verbose_name='设备种类', on_delete=models.CASCADE, related_name="devices")
    name = models.CharField(verbose_name='设备名称', max_length=100)
    model = models.CharField(verbose_name='型号', max_length=100)
    device_id = models.CharField(verbose_name='出厂编号', max_length=100, blank=True)
    parameters = models.TextField(verbose_name='参数', blank=True)
    manufacturer = models.CharField(verbose_name='制造商', max_length=100, blank=True)
    vender = models.ForeignKey( Vender, verbose_name='供货商', on_delete=models.CASCADE, related_name='vender_devices')
    contract = models.CharField(verbose_name='合同', max_length=100, blank=True)
    buy_date = models.DateField(verbose_name='购买日期')
    department = models.CharField(verbose_name='使用科室', max_length=100, blank=True)
    keeper = models.CharField(verbose_name='保管人', max_length=100, blank=True)
    price = models.DecimalField(verbose_name='价格', max_digits=10, decimal_places=2)
    #calibration = models.CharField(verbose_name='校准', max_length=100)
    make_date = models.DateField(verbose_name='制造日期', blank=True, null=True)
    release_date = models.DateField(verbose_name='出厂日期', blank=True, null=True)
    arrival_date = models.DateField(verbose_name='到货日期', blank=True, null=True)
    use_date = models.DateField(verbose_name='启用日期', blank=True, null=True)
    demo = models.TextField(verbose_name='备注', blank=True)
    attachment = models.FileField(verbose_name='附件', upload_to='divces/attachments/', blank=True)
    
    class Meta:
        verbose_name = '设备'
        verbose_name_plural = '设备'
    
    def __str__(self):
        return self.name


class Calibration(models.Model):

    calibration_type = models.CharField(verbose_name='检定校准类型', max_length=40)
    org = models.ForeignKey(Vender,verbose_name='校准组织', on_delete=models.CASCADE, related_name='vender')
    book_number = models.CharField(verbose_name='校准证书号', max_length=40)
    device = models.ForeignKey(Device,verbose_name='设备',  on_delete=models.CASCADE, related_name='device')
    from_date = models.DateField(verbose_name='校准日期')
    expired_date = models.DateField(verbose_name='到期日期')
    period_date = models.FloatField(verbose_name='校准周期')
    conclusion = models.CharField(verbose_name='结论', max_length=30)
    
    class Meta:

        verbose_name = '校准证书'
        verbose_name_plural = '校准证书'


    def __str__(self):
    
        return '校准证书({})'.format(self.book_number)
