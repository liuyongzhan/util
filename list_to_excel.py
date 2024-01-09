
res_list = [{'provider': 'tencent', 'origin_vm_type': 'S3.SMALL2', 'zone': 'ap-singapore-1', 'solution_id': 571,
             'run_id': 10131},
            {'provider': 'tencent', 'origin_vm_type': 'S2.SMALL2', 'zone': 'ap-singapore-1', 'solution_id': 571,
             'run_id': 10132},
            {'provider': 'tencent', 'origin_vm_type': 'S5.SMALL1', 'zone': 'ap-singapore-1', 'solution_id': 571,
             'run_id': 10133},
            {'provider': 'tencent', 'origin_vm_type': 'S1.SMALL2', 'zone': 'ap-singapore-1', 'solution_id': 571,
             'run_id': 10134},
            {'provider': 'tencent', 'origin_vm_type': 'S1.SMALL1', 'zone': 'ap-singapore-1', 'solution_id': 571,
             'run_id': 10135},
            {'provider': 'tencent', 'origin_vm_type': 'SA2.SMALL2', 'zone': 'ap-singapore-2', 'solution_id': 571,
             'run_id': 10136},
            {'provider': 'tencent', 'origin_vm_type': 'S3.SMALL1', 'zone': 'ap-singapore-1', 'solution_id': 571,
             'run_id': 10137},
            {'provider': 'tencent', 'origin_vm_type': 'SA2.SMALL1', 'zone': 'ap-singapore-2', 'solution_id': 571,
             'run_id': 10138},
            {'provider': 'tencent', 'origin_vm_type': 'S2.MEDIUM2', 'zone': 'eu-frankfurt-1', 'solution_id': 571,
             'run_id': 10139}]

if __name__ == '__main__':
    import pandas as pd
    import datetime
    now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    df = pd.DataFrame(res_list)
    df.to_excel('{}.xlsx'.format(now), index=False)
