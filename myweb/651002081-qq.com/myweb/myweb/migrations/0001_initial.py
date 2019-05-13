# Generated by Django 2.0 on 2019-05-09 13:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cmdb',
            fields=[
                ('Sn', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='sn')),
                ('Hostname', models.CharField(max_length=30, verbose_name='主机名')),
                ('OsVersion', models.CharField(max_length=20, verbose_name='操作系统版本')),
                ('Ip', models.CharField(max_length=15, verbose_name='ip')),
                ('Netmask', models.CharField(max_length=20, verbose_name='子网掩码')),
                ('GW', models.CharField(max_length=20, verbose_name='网关')),
                ('Mac', models.CharField(max_length=20, verbose_name='mac地址')),
                ('iLoIp', models.CharField(max_length=15, verbose_name='带外ip')),
                ('iLoNetmask', models.CharField(max_length=15, verbose_name='带外子网掩码')),
                ('iLoGW', models.CharField(max_length=15, verbose_name='带外网关')),
                ('iLoMac', models.CharField(max_length=10, verbose_name='带外mac')),
            ],
            options={
                'verbose_name': 'Cmdb',
                'verbose_name_plural': 'Cmdb',
                'ordering': ['Ip'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('TaskID', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='任务ID')),
                ('Taskname', models.CharField(max_length=20, verbose_name='任务名称')),
                ('Starttime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='开始时间')),
                ('Taksstatus', models.CharField(max_length=15, verbose_name='任务状态')),
                ('Completiontime', models.CharField(blank=True, max_length=20, null=True, verbose_name='结束时间')),
                ('Cmdb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myweb.Cmdb')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Task',
                'ordering': ['Starttime'],
            },
        ),
        migrations.CreateModel(
            name='TaskInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TaskDetail', models.CharField(blank=True, max_length=200, null=True, verbose_name='任务详情')),
            ],
            options={
                'verbose_name': 'TaskInfo',
                'verbose_name_plural': 'TaskInfo',
            },
        ),
        migrations.AddField(
            model_name='task',
            name='Taskinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myweb.TaskInfo'),
        ),
    ]