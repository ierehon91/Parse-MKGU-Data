def get_style():
    border = 'border: 1px solid #000000; border-collapse: collapse;'

    style = dict()
    style['body'] = 'font-family: Arial, sans-serif;'

    style['table'] = f'{border} color: #2C2A29; font-size: 13px;'

    style['thead'] = f''
    style['thead_tr'] =f''
    style['th_filial_name'] = f'{border}'
    style['th_count_phone_numbers'] = f'{border}'
    style['th_count_factors'] = f'{border}'
    style['th_all_scores'] = f'{border}'
    style['th_score_1'] = f'{border}'
    style['th_score_2'] = f'{border}'
    style['th_score_3'] = f'{border}'
    style['th_score_4'] = f'{border}'
    style['th_score_5'] = f'{border}'
    style['th_rating'] = f'{border}'

    style['tbody'] = f''
    style['tbody_tr'] = f'text-align: center'
    style['td_filial_name'] = f'{border} text-align: left'
    style['td_count_phone_numbers'] = f'{border}'
    style['td_count_factors'] = f'{border}'
    style['td_all_scores'] = f'{border}'
    style['td_score_1'] = f'{border}'
    style['td_score_2'] = f'{border}'
    style['td_score_3'] = f'{border}'
    style['td_score_4'] = f'{border}'
    style['td_score_5'] = f'{border}'
    style['td_rating'] = f'{border}'

    style['program_name'] = f''
    style['author'] = f''

    return style
