def get_style():
    border = 'border: 1px solid #E7D4C2; border-collapse: collapse;'
    bad_scores_background = 'background-color: #FDF3F3;'
    good_scores_background = 'background-color: #EEFFEE;'

    style = dict()
    style['body'] = 'font-family: Arial, sans-serif;'

    style['table'] = f'{border} color: #2C2A29;'

    style['thead'] = f'background-color: #F3F3F3; font-size: 12px; text-align: left; font-weight: normal;'
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

    style['tbody'] = f'font-size: 12px;'
    style['tbody_tr'] = f'text-align: center;'
    style['td_filial_name'] = f'{border} text-align: left;'
    style['td_count_phone_numbers'] = f'{border}'
    style['td_count_factors'] = f'{border}'
    style['td_all_scores'] = f'{border}'
    style['td_score_1'] = f'{border} {bad_scores_background}'
    style['td_score_2'] = f'{border} {bad_scores_background}'
    style['td_score_3'] = f'{border} {bad_scores_background}'
    style['td_score_4'] = f'{border} {good_scores_background}'
    style['td_score_5'] = f'{border} {good_scores_background}'
    style['td_rating'] = f'{border}'

    style['program_name'] = f'font-size: 15px; color: #2C2A29;'
    style['author'] = f'font-size: 13px; color: #2C2A29;'

    return style
