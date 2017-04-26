# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 13:49
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContaBancaria',
            fields=[
                ('contaBancariaId', models.AutoField(primary_key=True, serialize=False)),
                ('classificacao', models.CharField(max_length=18, verbose_name='Classificação')),
                ('descricao', models.CharField(max_length=50)),
                ('numeroAgencia', models.CharField(max_length=20, verbose_name='Agência')),
                ('numeroConta', models.CharField(max_length=20, verbose_name='Conta')),
                ('dataSaldoInicial', models.DateField()),
                ('saldoIncial_currency', djmoney.models.fields.CurrencyField(choices=[('AFN', 'Afghani'), ('DZD', 'Algerian Dinar'), ('ARS', 'Argentine Peso'), ('AMD', 'Armenian Dram'), ('AWG', 'Aruban Guilder'), ('AUD', 'Australian Dollar'), ('AZN', 'Azerbaijanian Manat'), ('BSD', 'Bahamian Dollar'), ('BHD', 'Bahraini Dinar'), ('THB', 'Baht'), ('BBD', 'Barbados Dollar'), ('BYR', 'Belarussian Ruble'), ('BZD', 'Belize Dollar'), ('BMD', 'Bermudian Dollar (customarily known as Bermuda Dollar)'), ('BTN', 'Bhutanese ngultrum'), ('VEF', 'Bolivar Fuerte'), ('XBA', 'Bond Markets Units European Composite Unit (EURCO)'), ('BRL', 'Brazilian Real'), ('BND', 'Brunei Dollar'), ('BGN', 'Bulgarian Lev'), ('BIF', 'Burundi Franc'), ('XOF', 'CFA Franc BCEAO'), ('XAF', 'CFA franc BEAC'), ('XPF', 'CFP Franc'), ('CAD', 'Canadian Dollar'), ('CVE', 'Cape Verde Escudo'), ('KYD', 'Cayman Islands Dollar'), ('CLP', 'Chilean peso'), ('XTS', 'Codes specifically reserved for testing purposes'), ('COP', 'Colombian peso'), ('KMF', 'Comoro Franc'), ('CDF', 'Congolese franc'), ('BAM', 'Convertible Marks'), ('NIO', 'Cordoba Oro'), ('CRC', 'Costa Rican Colon'), ('HRK', 'Croatian Kuna'), ('CUP', 'Cuban Peso'), ('CUC', 'Cuban convertible peso'), ('CZK', 'Czech Koruna'), ('GMD', 'Dalasi'), ('DKK', 'Danish Krone'), ('MKD', 'Denar'), ('DJF', 'Djibouti Franc'), ('STD', 'Dobra'), ('DOP', 'Dominican Peso'), ('VND', 'Dong'), ('XCD', 'East Caribbean Dollar'), ('EGP', 'Egyptian Pound'), ('ETB', 'Ethiopian Birr'), ('EUR', 'Euro'), ('XBB', 'European Monetary Unit (E.M.U.-6)'), ('XBD', 'European Unit of Account 17(E.U.A.-17)'), ('XBC', 'European Unit of Account 9(E.U.A.-9)'), ('FKP', 'Falkland Islands Pound'), ('FJD', 'Fiji Dollar'), ('HUF', 'Forint'), ('GHS', 'Ghana Cedi'), ('GIP', 'Gibraltar Pound'), ('XAU', 'Gold'), ('XFO', 'Gold-Franc'), ('PYG', 'Guarani'), ('GNF', 'Guinea Franc'), ('GYD', 'Guyana Dollar'), ('HTG', 'Haitian gourde'), ('HKD', 'Hong Kong Dollar'), ('UAH', 'Hryvnia'), ('ISK', 'Iceland Krona'), ('INR', 'Indian Rupee'), ('IRR', 'Iranian Rial'), ('IQD', 'Iraqi Dinar'), ('IMP', 'Isle of Man pount'), ('JMD', 'Jamaican Dollar'), ('JOD', 'Jordanian Dinar'), ('KES', 'Kenyan Shilling'), ('PGK', 'Kina'), ('LAK', 'Kip'), ('KWD', 'Kuwaiti Dinar'), ('AOA', 'Kwanza'), ('MMK', 'Kyat'), ('GEL', 'Lari'), ('LVL', 'Latvian Lats'), ('LBP', 'Lebanese Pound'), ('ALL', 'Lek'), ('HNL', 'Lempira'), ('SLL', 'Leone'), ('LSL', 'Lesotho loti'), ('LRD', 'Liberian Dollar'), ('LYD', 'Libyan Dinar'), ('SZL', 'Lilangeni'), ('LTL', 'Lithuanian Litas'), ('MGA', 'Malagasy Ariary'), ('MWK', 'Malawian Kwacha'), ('MYR', 'Malaysian Ringgit'), ('TMM', 'Manat'), ('MUR', 'Mauritius Rupee'), ('MZN', 'Metical'), ('MXN', 'Mexican peso'), ('MDL', 'Moldovan Leu'), ('MAD', 'Moroccan Dirham'), ('NGN', 'Naira'), ('ERN', 'Nakfa'), ('NAD', 'Namibian Dollar'), ('NPR', 'Nepalese Rupee'), ('ANG', 'Netherlands Antillian Guilder'), ('ILS', 'New Israeli Sheqel'), ('RON', 'New Leu'), ('TWD', 'New Taiwan Dollar'), ('NZD', 'New Zealand Dollar'), ('KPW', 'North Korean Won'), ('NOK', 'Norwegian Krone'), ('PEN', 'Nuevo Sol'), ('MRO', 'Ouguiya'), ('TOP', 'Paanga'), ('PKR', 'Pakistan Rupee'), ('XPD', 'Palladium'), ('MOP', 'Pataca'), ('PHP', 'Philippine Peso'), ('XPT', 'Platinum'), ('GBP', 'Pound Sterling'), ('BWP', 'Pula'), ('QAR', 'Qatari Rial'), ('GTQ', 'Quetzal'), ('ZAR', 'Rand'), ('OMR', 'Rial Omani'), ('KHR', 'Riel'), ('MVR', 'Rufiyaa'), ('IDR', 'Rupiah'), ('RUB', 'Russian Ruble'), ('RWF', 'Rwanda Franc'), ('XDR', 'SDR'), ('SHP', 'Saint Helena Pound'), ('SAR', 'Saudi Riyal'), ('RSD', 'Serbian Dinar'), ('SCR', 'Seychelles Rupee'), ('XAG', 'Silver'), ('SGD', 'Singapore Dollar'), ('SBD', 'Solomon Islands Dollar'), ('KGS', 'Som'), ('SOS', 'Somali Shilling'), ('TJS', 'Somoni'), ('LKR', 'Sri Lanka Rupee'), ('SDG', 'Sudanese Pound'), ('SRD', 'Surinam Dollar'), ('SEK', 'Swedish Krona'), ('CHF', 'Swiss Franc'), ('SYP', 'Syrian Pound'), ('BDT', 'Taka'), ('WST', 'Tala'), ('TZS', 'Tanzanian Shilling'), ('KZT', 'Tenge'), ('TTD', 'Trinidad and Tobago Dollar'), ('MNT', 'Tugrik'), ('TND', 'Tunisian Dinar'), ('TRY', 'Turkish Lira'), ('TVD', 'Tuvalu dollar'), ('AED', 'UAE Dirham'), ('XFU', 'UIC-Franc'), ('USD', 'US Dollar'), ('UGX', 'Uganda Shilling'), ('UYU', 'Uruguayan peso'), ('UZS', 'Uzbekistan Sum'), ('VUV', 'Vatu'), ('KRW', 'Won'), ('YER', 'Yemeni Rial'), ('JPY', 'Yen'), ('CNY', 'Yuan Renminbi'), ('ZMK', 'Zambian Kwacha'), ('ZMW', 'Zambian Kwacha'), ('ZWD', 'Zimbabwe Dollar A/06'), ('ZWN', 'Zimbabwe dollar A/08'), ('ZWL', 'Zimbabwe dollar A/09'), ('PLN', 'Zloty')], default='BRL', editable=False, max_length=3)),
                ('saldoIncial', djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0.0'), default_currency='BRL', max_digits=100)),
                ('caixa', models.CharField(max_length=1)),
                ('banco', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('EmpresaId', models.AutoField(primary_key=True, serialize=False)),
                ('razaoSocial', models.CharField(max_length=255)),
                ('inscricaoEstadual', models.CharField(max_length=20)),
                ('inscricaoMunicipal', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='FormaPagamento',
            fields=[
                ('FormaPagamentoId', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Muncipio',
            fields=[
                ('municipioId', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=255, verbose_name='Município')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('pessoaId', models.AutoField(primary_key=True, serialize=False)),
                ('classificacao', models.CharField(max_length=18)),
                ('indentificacao', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PlanoContas',
            fields=[
                ('planoContasId', models.AutoField(primary_key=True, serialize=False)),
                ('classificacao', models.CharField(max_length=18)),
                ('tipoConta', models.CharField(max_length=15)),
                ('descricao', models.CharField(max_length=50)),
                ('caixa', models.CharField(max_length=1)),
                ('banco', models.CharField(max_length=1)),
                ('cliente', models.CharField(max_length=1)),
                ('fornecedor', models.CharField(max_length=1)),
                ('entradaRecurso', models.CharField(max_length=1)),
                ('saidaRecurso', models.CharField(max_length=1)),
                ('contaCancariaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.ContaBancaria')),
            ],
        ),
        migrations.CreateModel(
            name='Uf',
            fields=[
                ('ufId', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=50, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cadastros.Pessoa')),
                ('cpf', models.CharField(max_length=11)),
            ],
            bases=('cadastros.pessoa',),
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cadastros.Pessoa')),
                ('cnpj', models.CharField(max_length=15)),
                ('inscricaoEstadual', models.CharField(max_length=20)),
                ('inscricaoMunicipal', models.CharField(max_length=20)),
            ],
            bases=('cadastros.pessoa',),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='municipioID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.Muncipio'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='ufId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.Uf', verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='muncipio',
            name='ufId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.Uf', verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='municipioID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.Muncipio'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='ufId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.Uf'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='titularId',
            field=models.ForeignKey(on_delete='pessoa_ptr', to='cadastros.PessoaJuridica', to_field='pessoaId'),
        ),
    ]
