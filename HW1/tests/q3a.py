test = {   'name': 'q3a',
    'points': 10,
    'suites': [   {   'cases': [   {   'code': '>>> from torchsummary import summary\n'
                                               '>>> summary(model, (1, 28, 28))\n'
                                               '----------------------------------------------------------------\n'
                                               '        Layer (type)               Output Shape         Param #\n'
                                               '================================================================\n'
                                               '            Conv2d-1           [-1, 32, 28, 28]             832\n'
                                               '       BatchNorm2d-2           [-1, 32, 28, 28]              64\n'
                                               '              ReLU-3           [-1, 32, 28, 28]               0\n'
                                               '         AvgPool2d-4           [-1, 32, 14, 14]               0\n'
                                               '            Conv2d-5           [-1, 32, 14, 14]          25,632\n'
                                               '       BatchNorm2d-6           [-1, 32, 14, 14]              64\n'
                                               '              ReLU-7           [-1, 32, 14, 14]               0\n'
                                               '         AvgPool2d-8             [-1, 32, 7, 7]               0\n'
                                               '            Conv2d-9             [-1, 64, 7, 7]          51,264\n'
                                               '      BatchNorm2d-10             [-1, 64, 7, 7]             128\n'
                                               '             ReLU-11             [-1, 64, 7, 7]               0\n'
                                               '        AvgPool2d-12             [-1, 64, 3, 3]               0\n'
                                               '           Linear-13                   [-1, 64]          36,928\n'
                                               '      BatchNorm1d-14                   [-1, 64]             128\n'
                                               '             ReLU-15                   [-1, 64]               0\n'
                                               '           Linear-16                   [-1, 10]             650\n'
                                               '================================================================\n'
                                               'Total params: 115,690\n'
                                               'Trainable params: 115,690\n'
                                               'Non-trainable params: 0\n'
                                               '----------------------------------------------------------------\n'
                                               'Input size (MB): 0.00\n'
                                               'Forward/backward pass size (MB): 0.86\n'
                                               'Params size (MB): 0.44\n'
                                               'Estimated Total Size (MB): 1.30\n'
                                               '----------------------------------------------------------------\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
