1. PRD
2. TEST
3. DEV
�ͳθ���Ʈ ellt1: 54423
�ͳθ���Ʈ ltcm1: 54425
�ͳθ���Ʈ ellt2: 54427
�ͳθ���Ʈ ellt3: 54429
�ͳθ���Ʈ ellt4: 54431
�ͳθ���Ʈ ellt5: 54433
�ͳθ���Ʈ ellt6: 54437
[('elltprtst', 'cc_intrst_mbr_dtl_out'), ('elltprtst', 'dp_dshop_dgoods_out'), ('elltprtst', 'dp_dshop_out'), ('ltcmattst', 'dp_scat_out'), ('elltlotst', 'et_entprz_hldy_out'), ('elltdptst', 'et_entshp_out'), ('elltprtst', 'et_entshp_out'), ('elltomtst', 'et_entshp_out'), ('elltomtst', 'et_entshp_owh_wtgval_out'), ('elltdptst', 'et_sup_entprz_out'), ('elltprtst', 'et_sup_entprz_out'), ('elltomtst', 'et_sup_entprz_owh_wtgval_out'), ('elltomtst', 'et_sup_entprz_prior_owh_out'), ('elltdptst', 'gd_brnd_conts_out'), ('elltdptst', 'gd_brnd_out'), ('elltprtst', 'gd_brnd_out'), ('elltcmtst', 'gd_brnd_out'), ('elltdptst', 'gd_goods_out'), ('ltcmattst', 'gd_goods_out'), ('elltprtst', 'gd_goods_out'), ('elltdptst', 'gd_goods_prc_out'), ('elltdptst', 'gd_goods_smry_out'), ('elltprtst', 'gd_goods_smry_out'), ('elltdptst', 'gd_item_sup_entprz_stk_out'), ('elltdptst', 'gd_md_gsgr_out'), ('elltprtst', 'gd_md_gsgr_out'), ('elltdptst', 'gd_sup_entprz_magn_out'), ('elltombqtst', 'lo_claim_dlv_out'), ('elltombqtst', 'lo_ord_dlv_out'), ('elltprtst', 'mb_ec_cust_out'), ('elltprtst', 'mb_mbr_grd_out'), ('elltsetst', 'om_claim_dtl_out'), ('elltombqtst', 'om_claim_dtl_out'), ('elltombqtst', 'om_claim_out'), ('elltsetst', 'om_ord_dtl_out'), ('elltombqtst', 'om_ord_dtl_out'), ('elltsetst', 'om_ord_exp_goods_out'), ('elltombqtst', 'om_ord_exp_goods_out'), ('elltsetst', 'om_ord_exp_out'), ('elltombqtst', 'om_ord_exp_out'), ('elltsetst', 'om_ord_fvr_out'), ('elltombqtst', 'om_ord_fvr_out'), ('elltombqtst', 'om_ord_out'), ('elltdptst', 'pr_cmpn_dc_goods_smry_out'), ('elltgdtst', 'pr_cmpn_dc_goods_smry_out'), ('elltdptst', 'pr_dc_xclud_goods_out'), ('elltgdtst', 'pr_dc_xclud_goods_out'), ('elltsetst', 'py_mbsh_point_if_out'), ('elltsetst', 'py_pyf_out'), ('elltombqtst', 'py_pyf_out')]
############ elltcctst.cc_intrst_mbr_dtl -> elltprtst.cc_intrst_mbr_dtl_out##############

############ elltdptst.dp_dshop_dgoods -> elltprtst.dp_dshop_dgoods_out##############

############ elltdptst.dp_dshop -> elltprtst.dp_dshop_out##############
#�ҽ�: ELLTDPTST, ���̺� - DP_DSHOP, �÷�- RNKH_DSHOP_NO, type- int(5), CHARSET- None, Ŀ��Ʈ- �������ø����ȣ, , IS_NULLABLE- NO
#Ÿ��: ELLTPRTST, ���̺� - DP_DSHOP_OUT, �÷�- RNKH_DSHOP_NO, type- int(5), CHARSET- None, Ŀ��Ʈ- �������ø����ȣ, , IS_NULLABLE- YES
ALTER TABLE ELLTPRTST.DP_DSHOP_OUT CHANGE COLUMN `RNKH_DSHOP_NO` 
`RNKH_DSHOP_NO` int(5) NOT NULL 
comment '�������ø����ȣ';

############ elltdptst.dp_scat -> ltcmattst.dp_scat_out##############

############ elltettst.et_entprz_hldy -> elltlotst.et_entprz_hldy_out##############
#�ҽ�: ELLTETTST, ���̺� - ET_ENTPRZ_HLDY, �÷�- MODR_ID, type- varchar(30), CHARSET- utf8_general_ci, Ŀ��Ʈ- �����ھ��̵�, , IS_NULLABLE- NO
#Ÿ��: ELLTLOTST, ���̺� - ET_ENTPRZ_HLDY_OUT, �÷�- MODR_ID, type- varchar(30), CHARSET- utf8_general_ci, Ŀ��Ʈ- �����ھ��̵�, , IS_NULLABLE- YES
ALTER TABLE ELLTLOTST.ET_ENTPRZ_HLDY_OUT CHANGE COLUMN `MODR_ID` 
`MODR_ID` varchar(30) NOT NULL 
comment '�����ھ��̵�';
#�ҽ�: ELLTETTST, ���̺� - ET_ENTPRZ_HLDY, �÷�- MODI_DTTM, type- datetime, CHARSET- None, Ŀ��Ʈ- �����Ͻ�, , IS_NULLABLE- NO
#Ÿ��: ELLTLOTST, ���̺� - ET_ENTPRZ_HLDY_OUT, �÷�- MODI_DTTM, type- datetime, CHARSET- None, Ŀ��Ʈ- �����Ͻ�, , IS_NULLABLE- YES
ALTER TABLE ELLTLOTST.ET_ENTPRZ_HLDY_OUT CHANGE COLUMN `MODI_DTTM` 
`MODI_DTTM` datetime NOT NULL 
comment '�����Ͻ�';

############ elltettst.et_entshp -> elltdptst.et_entshp_out##############
#�ҽ�: ELLTETTST, ���̺� - ET_ENTSHP, �÷�- HMPG_URL, type- varchar(150), CHARSET- utf8_general_ci, Ŀ��Ʈ- Ȩ������URL, , IS_NULLABLE- YES
#Ÿ��: ELLTDPTST, ���̺� - ET_ENTSHP_OUT, �÷�- HMPG_URL, type- varchar(150), CHARSET- ucs2_general_ci, Ŀ��Ʈ- , , IS_NULLABLE- YES
ALTER TABLE ELLTDPTST.ET_ENTSHP_OUT CHANGE COLUMN `HMPG_URL` 
`HMPG_URL` varchar(150)  NULL 
comment 'Ȩ������URL';
#�ҽ�: ELLTETTST, ���̺� - ET_ENTSHP, �÷�- ENTSHP_GROUP_DVS_CD, type- varchar(20), CHARSET- utf8_general_ci, Ŀ��Ʈ- �����׷챸���ڵ�, , IS_NULLABLE- YES
#Ÿ��: ELLTDPTST, ���̺� - ET_ENTSHP_OUT, �÷�- ENTSHP_GROUP_DVS_CD, type- varchar(20), CHARSET- ucs2_general_ci, Ŀ��Ʈ- , , IS_NULLABLE- YES
ALTER TABLE ELLTDPTST.ET_ENTSHP_OUT CHANGE COLUMN `ENTSHP_GROUP_DVS_CD` 
`ENTSHP_GROUP_DVS_CD` varchar(20)  NULL 
comment '�����׷챸���ڵ�';
#�ҽ�: ELLTETTST, ���̺� - ET_ENTSHP, �÷�- ENTSHP_RGN_DVS_CD, type- varchar(20), CHARSET- utf8_general_ci, Ŀ��Ʈ- �������������ڵ�, , IS_NULLABLE- YES
#Ÿ��: ELLTDPTST, ���̺� - ET_ENTSHP_OUT, �÷�- ENTSHP_RGN_DVS_CD, type- varchar(20), CHARSET- ucs2_general_ci, Ŀ��Ʈ- , , IS_NULLABLE- YES
ALTER TABLE ELLTDPTST.ET_ENTSHP_OUT CHANGE COLUMN `ENTSHP_RGN_DVS_CD` 
`ENTSHP_RGN_DVS_CD` varchar(20)  NULL 
comment '�������������ڵ�';
#�ҽ�: ELLTETTST, ���̺� - ET_ENTSHP, �÷�- RGSTR_ID, type- varchar(30), CHARSET- utf8_general_ci, Ŀ��Ʈ- ����ھ��̵�, , IS_NULLABLE- NO
#Ÿ��: ELLTDPTST, ���̺� - ET_ENTSHP_OUT, �÷�- RGSTR_ID, type- varchar(30), CHARSET- ucs2_general_ci, Ŀ��Ʈ- , , IS_NULLABLE- YES
ALTER TABLE ELLTDPTST.ET_ENTSHP_OUT CHANGE COLUMN `RGSTR_ID` 
`RGSTR_ID` varchar(30) NOT NULL 
comment '����ھ��̵�';
#�ҽ�: ELLTETTST, ���̺� - ET_ENTSHP, �÷�- RGSTR_NM, type- varchar(30), CHARSET- utf8_general_ci, Ŀ��Ʈ- ����ڸ�, , IS_NULLABLE- YES
#Ÿ��: ELLTDPTST, ���̺� - ET_ENTSHP_OUT, �÷�- RGSTR_NM, type- varchar(30), CHARSET- ucs2_general_ci, Ŀ��Ʈ- , , IS_NULLABLE- YES
ALTER TABLE ELLTDPTST.ET_ENTSHP_OUT CHANGE COLUMN `RGSTR_NM` 
`RGSTR_NM` varchar(30)  NULL 
comment '����ڸ�';
#�ҽ�: ELLTETTST, ���̺� - ET_ENTSHP, �÷�- RGST_DTTM, type- datetime, CHARSET- None, Ŀ��Ʈ- ����Ͻ�, , IS_NULLABLE- NO
#Ÿ��: ELLTDPTST, ���̺� - ET_ENTSHP_OUT, �÷�- RGST_DTTM, type- datetime, CHARSET- None, Ŀ��Ʈ- , , IS_NULLABLE- YES
ALTER TABLE ELLTDPTST.ET_ENTSHP_OUT CHANGE COLUMN `RGST_DTTM` 
`RGST_DTTM` datetime NOT NULL 
comment '����Ͻ�';
#�ҽ�: ELLTETTST, ���̺� - ET_ENTSHP, �÷�- MODR_ID, type- varchar(30), CHARSET- utf8_general_ci, Ŀ��Ʈ- �����ھ��̵�, , IS_NULLABLE- NO
#Ÿ��: ELLTDPTST, ���̺� - ET_ENTSHP_OUT, �÷�- MODR_ID, type- varchar(30), CHARSET- ucs2_general_ci, Ŀ��Ʈ- , , IS_NULLABLE- YES
ALTER TABLE ELLTDPTST.ET_ENTSHP_OUT CHANGE COLUMN `MODR_ID` 
`MODR_ID` varchar(30) NOT NULL 
comment '�����ھ��̵�';
#�ҽ�: ELLTETTST, ���̺� - ET_ENTSHP, �÷�- MODR_NM, type- varchar(30), CHARSET- utf8_general_ci, Ŀ��Ʈ- �����ڸ�, , IS_NULLABLE- YES
#Ÿ��: ELLTDPTST, ���̺� - ET_ENTSHP_OUT, �÷�- MODR_NM, type- varchar(30), CHARSET- ucs2_general_ci, Ŀ��Ʈ- , , IS_NULLABLE- YES
ALTER TABLE ELLTDPTST.ET_ENTSHP_OUT CHANGE COLUMN `MODR_NM` 
`MODR_NM` varchar(30)  NULL 
comment '�����ڸ�';
#�ҽ�: ELLTETTST, ���̺� - ET_ENTSHP, �÷�- MODI_DTTM, type- datetime, CHARSET- None, Ŀ��Ʈ- �����Ͻ�, , IS_NULLABLE- NO
#Ÿ��: ELLTDPTST, ���̺� - ET_ENTSHP_OUT, �÷�- MODI_DTTM, type- datetime, CHARSET- None, Ŀ��Ʈ- , , IS_NULLABLE- YES
ALTER TABLE ELLTDPTST.ET_ENTSHP_OUT CHANGE COLUMN `MODI_DTTM` 
`MODI_DTTM` datetime NOT NULL 
comment '�����Ͻ�';

############ elltettst.et_entshp -> elltprtst.et_entshp_out##############

############ elltettst.et_entshp -> elltomtst.et_entshp_out##############

############ elltettst.et_entshp_owh_wtgval -> elltomtst.et_entshp_owh_wtgval_out##############

############ elltettst.et_sup_entprz -> elltdptst.et_sup_entprz_out##############
#�ҽ�: ELLTETTST, ���̺� - ET_SUP_ENTPRZ, �÷�- RGSTR_NM, type- varchar(30), CHARSET- utf8_general_ci, Ŀ��Ʈ- ����ڸ�, , IS_NULLABLE- YES
#Ÿ��: ELLTDPTST, ���̺� - ET_SUP_ENTPRZ_OUT, �÷�- RGSTR_NM, type- varchar(30), CHARSET- ucs2_general_ci, Ŀ��Ʈ- , , IS_NULLABLE- YES
ALTER TABLE ELLTDPTST.ET_SUP_ENTPRZ_OUT CHANGE COLUMN `RGSTR_NM` 
`RGSTR_NM` varchar(30)  NULL 
comment '����ڸ�';
#�ҽ�: ELLTETTST, ���̺� - ET_SUP_ENTPRZ, �÷�- MODR_NM, type- varchar(30), CHARSET- utf8_general_ci, Ŀ��Ʈ- �����ڸ�, , IS_NULLABLE- YES
#Ÿ��: ELLTDPTST, ���̺� - ET_SUP_ENTPRZ_OUT, �÷�- MODR_NM, type- varchar(30), CHARSET- ucs2_general_ci, Ŀ��Ʈ- , , IS_NULLABLE- YES
ALTER TABLE ELLTDPTST.ET_SUP_ENTPRZ_OUT CHANGE COLUMN `MODR_NM` 
`MODR_NM` varchar(30)  NULL 
comment '�����ڸ�';

############ elltettst.et_sup_entprz -> elltprtst.et_sup_entprz_out##############

############ elltettst.et_sup_entprz_owh_wtgval -> elltomtst.et_sup_entprz_owh_wtgval_out##############

############ elltettst.et_sup_entprz_prior_owh -> elltomtst.et_sup_entprz_prior_owh_out##############

############ elltgdtst.gd_brnd_conts -> elltdptst.gd_brnd_conts_out##############
#�ҽ�: ELLTGDTST, ���̺� - GD_BRND_CONTS, �÷�- BRND_NO, type- int(7), CHARSET- None, Ŀ��Ʈ- �귣���ȣ, , IS_NULLABLE- NO
#Ÿ��: ELLTDPTST, ���̺� - GD_BRND_CONTS_OUT, �÷�- BRND_NO, type- int(10), CHARSET- None, Ŀ��Ʈ- �귣���ȣ, , IS_NULLABLE- NO
ALTER TABLE ELLTDPTST.GD_BRND_CONTS_OUT CHANGE COLUMN `BRND_NO` 
`BRND_NO` int(7) NOT NULL 
comment '�귣���ȣ';

############ elltgdtst.gd_brnd -> elltdptst.gd_brnd_out##############
#�ҽ�: ELLTGDTST, ���̺� - GD_BRND, �÷�- USE_YN, type- varchar(1), CHARSET- utf8_general_ci, Ŀ��Ʈ- ��뿩��, , IS_NULLABLE- NO
#Ÿ��: ELLTDPTST, ���̺� - GD_BRND_OUT, �÷�- USE_YN, type- varchar(1), CHARSET- utf8_general_ci, Ŀ��Ʈ- , , IS_NULLABLE- NO
ALTER TABLE ELLTDPTST.GD_BRND_OUT CHANGE COLUMN `USE_YN` 
`USE_YN` varchar(1) NOT NULL 
comment '��뿩��';

############ elltgdtst.gd_brnd -> elltprtst.gd_brnd_out##############

############ elltgdtst.gd_brnd -> elltcmtst.gd_brnd_out##############

############ elltgdtst.gd_goods -> elltdptst.gd_goods_out##############
#�ҽ�: ELLTGDTST, ���̺� - GD_GOODS, �÷�- SL_STAT_CD, type- varchar(20), CHARSET- utf8_general_ci, Ŀ��Ʈ- �ǸŻ����ڵ�, , IS_NULLABLE- NO
#Ÿ��: ELLTDPTST, ���̺� - GD_GOODS_OUT, �÷�- SL_STAT_CD, type- varchar(20), CHARSET- utf8_general_ci, Ŀ��Ʈ- , , IS_NULLABLE- NO
ALTER TABLE ELLTDPTST.GD_GOODS_OUT CHANGE COLUMN `SL_STAT_CD` 
`SL_STAT_CD` varchar(20) NOT NULL 
comment '�ǸŻ����ڵ�';

############ elltgdtst.gd_goods -> ltcmattst.gd_goods_out##############

############ elltgdtst.gd_goods -> elltprtst.gd_goods_out##############

############ elltgdtst.gd_goods_prc -> elltdptst.gd_goods_prc_out##############

############ elltgdtst.gd_goods_smry -> elltdptst.gd_goods_smry_out##############
#�ҽ�: ELLTGDTST, ���̺� - GD_GOODS_SMRY, �÷�- CUST_STFD_EVLSCR1, type- smallint(2), CHARSET- None, Ŀ��Ʈ- ������������1, , IS_NULLABLE- YES
#Ÿ��: ELLTDPTST, ���̺� - GD_GOODS_SMRY_OUT, �÷�- CUST_STFD_EVLSCR1, type- smallint(6), CHARSET- None, Ŀ��Ʈ- ������������1, , IS_NULLABLE- YES
ALTER TABLE ELLTDPTST.GD_GOODS_SMRY_OUT CHANGE COLUMN `CUST_STFD_EVLSCR1` 
`CUST_STFD_EVLSCR1` smallint(2)  NULL 
comment '������������1';
#�ҽ�: ELLTGDTST, ���̺� - GD_GOODS_SMRY, �÷�- CUST_STFD_EVLSCR2, type- smallint(2), CHARSET- None, Ŀ��Ʈ- ������������2, , IS_NULLABLE- YES
#Ÿ��: ELLTDPTST, ���̺� - GD_GOODS_SMRY_OUT, �÷�- CUST_STFD_EVLSCR2, type- smallint(6), CHARSET- None, Ŀ��Ʈ- ������������2, , IS_NULLABLE- YES
ALTER TABLE ELLTDPTST.GD_GOODS_SMRY_OUT CHANGE COLUMN `CUST_STFD_EVLSCR2` 
`CUST_STFD_EVLSCR2` smallint(2)  NULL 
comment '������������2';

############ elltgdtst.gd_goods_smry -> elltprtst.gd_goods_smry_out##############

############ elltgdtst.gd_item_sup_entprz_stk -> elltdptst.gd_item_sup_entprz_stk_out##############

############ elltgdtst.gd_md_gsgr -> elltdptst.gd_md_gsgr_out##############

############ elltgdtst.gd_md_gsgr -> elltprtst.gd_md_gsgr_out##############

############ elltgdtst.gd_sup_entprz_magn -> elltdptst.gd_sup_entprz_magn_out##############

############ elltlotst.lo_claim_dlv -> elltombqtst.lo_claim_dlv_out##############

############ elltlotst.lo_ord_dlv -> elltombqtst.lo_ord_dlv_out##############

############ elltmbtst.mb_ec_cust -> elltprtst.mb_ec_cust_out##############
#�ҽ�: ELLTMBTST, ���̺� - MB_EC_CUST, �÷�- CUST_NM, type- varchar(30), CHARSET- utf8_general_ci, Ŀ��Ʈ- ����, , IS_NULLABLE- NO
#Ÿ��: ELLTPRTST, ���̺� - MB_EC_CUST_OUT, �÷�- CUST_NM, type- varchar(30), CHARSET- utf8_general_ci, Ŀ��Ʈ- ����, , IS_NULLABLE- YES
ALTER TABLE ELLTPRTST.MB_EC_CUST_OUT CHANGE COLUMN `CUST_NM` 
`CUST_NM` varchar(30) NOT NULL 
comment '����';
#�ҽ�: ELLTMBTST, ���̺� - MB_EC_CUST, �÷�- MBR_LOGIN_ID, type- varchar(100), CHARSET- utf8_general_ci, Ŀ��Ʈ- ȸ���α��ξ��̵�, , IS_NULLABLE- NO
#Ÿ��: ELLTPRTST, ���̺� - MB_EC_CUST_OUT, �÷�- MBR_LOGIN_ID, type- varchar(100), CHARSET- utf8_general_ci, Ŀ��Ʈ- ȸ���α��ξ��̵�, , IS_NULLABLE- YES
ALTER TABLE ELLTPRTST.MB_EC_CUST_OUT CHANGE COLUMN `MBR_LOGIN_ID` 
`MBR_LOGIN_ID` varchar(100) NOT NULL 
comment 'ȸ���α��ξ��̵�';
#MB_EC_CUST_OUT:MBR_GRADE_CD �÷� �ҽ��� ����
ALTER TABLE ELLTPRTST.MB_EC_CUST_OUT drop column `MBR_GRADE_CD`;

############ elltmbtst.mb_mbr_grd -> elltprtst.mb_mbr_grd_out##############

############ elltomtst.om_claim_dtl -> elltsetst.om_claim_dtl_out##############
#�ҽ�: ELLTOMTST, ���̺� - OM_CLAIM_DTL, �÷�- EXTRNL_IF_NO, type- int(11), CHARSET- None, Ŀ��Ʈ- �ܺ��������̽���ȣ, , IS_NULLABLE- NO
#Ÿ��: ELLTSETST, ���̺� - OM_CLAIM_DTL_OUT, �÷�- EXTRNL_IF_NO, type- int(11), CHARSET- None, Ŀ��Ʈ- �ܺ��������̽���ȣ, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_CLAIM_DTL_OUT CHANGE COLUMN `EXTRNL_IF_NO` 
`EXTRNL_IF_NO` int(11) NOT NULL 
comment '�ܺ��������̽���ȣ';
#�ҽ�: ELLTOMTST, ���̺� - OM_CLAIM_DTL, �÷�- CLAIM_DLVPLC_GROUP_NO, type- int(11), CHARSET- None, Ŀ��Ʈ- Ŭ���ӹ�����׷��ȣ, , IS_NULLABLE- NO
#Ÿ��: ELLTSETST, ���̺� - OM_CLAIM_DTL_OUT, �÷�- CLAIM_DLVPLC_GROUP_NO, type- int(11), CHARSET- None, Ŀ��Ʈ- Ŭ���ӹ�����׷��ȣ, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_CLAIM_DTL_OUT CHANGE COLUMN `CLAIM_DLVPLC_GROUP_NO` 
`CLAIM_DLVPLC_GROUP_NO` int(11) NOT NULL 
comment 'Ŭ���ӹ�����׷��ȣ';

############ elltomtst.om_claim_dtl -> elltombqtst.om_claim_dtl_out##############

############ elltomtst.om_claim -> elltombqtst.om_claim_out##############

############ elltomtst.om_ord_dtl -> elltsetst.om_ord_dtl_out##############
#�ҽ�: ELLTOMTST, ���̺� - OM_ORD_DTL, �÷�- EXTRNL_IF_NO, type- int(11), CHARSET- None, Ŀ��Ʈ- �ܺ��������̽���ȣ, , IS_NULLABLE- NO
#Ÿ��: ELLTSETST, ���̺� - OM_ORD_DTL_OUT, �÷�- EXTRNL_IF_NO, type- int(11), CHARSET- None, Ŀ��Ʈ- �ܺ��������̽���ȣ, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_DTL_OUT CHANGE COLUMN `EXTRNL_IF_NO` 
`EXTRNL_IF_NO` int(11) NOT NULL 
comment '�ܺ��������̽���ȣ';
#�ҽ�: ELLTOMTST, ���̺� - OM_ORD_DTL, �÷�- ORD_DLVPLC_GROUP_NO, type- int(11), CHARSET- None, Ŀ��Ʈ- �ֹ�������׷��ȣ, , IS_NULLABLE- NO
#Ÿ��: ELLTSETST, ���̺� - OM_ORD_DTL_OUT, �÷�- ORD_DLVPLC_GROUP_NO, type- int(11), CHARSET- None, Ŀ��Ʈ- �ֹ�������׷��ȣ, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_DTL_OUT CHANGE COLUMN `ORD_DLVPLC_GROUP_NO` 
`ORD_DLVPLC_GROUP_NO` int(11) NOT NULL 
comment '�ֹ�������׷��ȣ';
#�ҽ�: ELLTOMTST, ���̺� - OM_ORD_DTL, �÷�- ORD_EXP_GROUP_NO, type- int(4), CHARSET- None, Ŀ��Ʈ- �ֹ����׷��ȣ, , IS_NULLABLE- NO
#Ÿ��: ELLTSETST, ���̺� - OM_ORD_DTL_OUT, �÷�- ORD_EXP_GROUP_NO, type- int(4), CHARSET- None, Ŀ��Ʈ- �ֹ����׷��ȣ, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_DTL_OUT CHANGE COLUMN `ORD_EXP_GROUP_NO` 
`ORD_EXP_GROUP_NO` int(4) NOT NULL 
comment '�ֹ����׷��ȣ';
#�ҽ�: ELLTOMTST, ���̺� - OM_ORD_DTL, �÷�- ORD_ALTMNT_GROUP_NO, type- smallint(6), CHARSET- None, Ŀ��Ʈ- �ֹ���б׷��ȣ, , IS_NULLABLE- NO
#Ÿ��: ELLTSETST, ���̺� - OM_ORD_DTL_OUT, �÷�- ORD_ALTMNT_GROUP_NO, type- smallint(6), CHARSET- None, Ŀ��Ʈ- �ֹ���б׷��ȣ, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_DTL_OUT CHANGE COLUMN `ORD_ALTMNT_GROUP_NO` 
`ORD_ALTMNT_GROUP_NO` smallint(6) NOT NULL 
comment '�ֹ���б׷��ȣ';
#�ҽ�: ELLTOMTST, ���̺� - OM_ORD_DTL, �÷�- SLPRC, type- int(10), CHARSET- None, Ŀ��Ʈ- �ǸŰ�, , IS_NULLABLE- NO
#Ÿ��: ELLTSETST, ���̺� - OM_ORD_DTL_OUT, �÷�- SLPRC, type- int(11), CHARSET- None, Ŀ��Ʈ- �ǸŰ�, , IS_NULLABLE- NO
ALTER TABLE ELLTSETST.OM_ORD_DTL_OUT CHANGE COLUMN `SLPRC` 
`SLPRC` int(10) NOT NULL 
comment '�ǸŰ�';
#�ҽ�: ELLTOMTST, ���̺� - OM_ORD_DTL, �÷�- STRPIC_LOC_CD, type- varchar(20), CHARSET- utf8_general_ci, Ŀ��Ʈ- ����Ʈ��ġ�ڵ�, , IS_NULLABLE- YES
#Ÿ��: ELLTSETST, ���̺� - OM_ORD_DTL_OUT, �÷�- STRPIC_LOC_CD, type- varchar(20), CHARSET- utf8_general_ci, Ŀ��Ʈ- ����Ʈ����ġ�ڵ�, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_DTL_OUT CHANGE COLUMN `STRPIC_LOC_CD` 
`STRPIC_LOC_CD` varchar(20)  NULL 
comment '����Ʈ��ġ�ڵ�';

############ elltomtst.om_ord_dtl -> elltombqtst.om_ord_dtl_out##############

############ elltomtst.om_ord_exp_goods -> elltsetst.om_ord_exp_goods_out##############
#�ҽ�: ELLTOMTST, ���̺� - OM_ORD_EXP_GOODS, �÷�- ORD_SEQ, type- int(11), CHARSET- None, Ŀ��Ʈ- �ֹ�����, , IS_NULLABLE- NO
#Ÿ��: ELLTSETST, ���̺� - OM_ORD_EXP_GOODS_OUT, �÷�- ORD_SEQ, type- int(11), CHARSET- None, Ŀ��Ʈ- �ֹ�����, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_EXP_GOODS_OUT CHANGE COLUMN `ORD_SEQ` 
`ORD_SEQ` int(11) NOT NULL 
comment '�ֹ�����';

############ elltomtst.om_ord_exp_goods -> elltombqtst.om_ord_exp_goods_out##############

############ elltomtst.om_ord_exp -> elltsetst.om_ord_exp_out##############
#�ҽ�: ELLTOMTST, ���̺� - OM_ORD_EXP, �÷�- DLV_EXP, type- int(10), CHARSET- None, Ŀ��Ʈ- ��ۺ��, , IS_NULLABLE- NO
#Ÿ��: ELLTSETST, ���̺� - OM_ORD_EXP_OUT, �÷�- DLV_EXP, type- int(10), CHARSET- None, Ŀ��Ʈ- ��ۺ��, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_EXP_OUT CHANGE COLUMN `DLV_EXP` 
`DLV_EXP` int(10) NOT NULL 
comment '��ۺ��';
#�ҽ�: ELLTOMTST, ���̺� - OM_ORD_EXP, �÷�- STD_AMT, type- int(11), CHARSET- None, Ŀ��Ʈ- ���رݾ�, , IS_NULLABLE- NO
#Ÿ��: ELLTSETST, ���̺� - OM_ORD_EXP_OUT, �÷�- STD_AMT, type- int(11), CHARSET- None, Ŀ��Ʈ- ���رݾ�, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_EXP_OUT CHANGE COLUMN `STD_AMT` 
`STD_AMT` int(11) NOT NULL 
comment '���رݾ�';
#�ҽ�: ELLTOMTST, ���̺� - OM_ORD_EXP, �÷�- RTN_EXP, type- int(10), CHARSET- None, Ŀ��Ʈ- ��ǰ���, , IS_NULLABLE- NO
#Ÿ��: ELLTSETST, ���̺� - OM_ORD_EXP_OUT, �÷�- RTN_EXP, type- int(10), CHARSET- None, Ŀ��Ʈ- ��ǰ���, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_EXP_OUT CHANGE COLUMN `RTN_EXP` 
`RTN_EXP` int(10) NOT NULL 
comment '��ǰ���';
#�ҽ�: ELLTOMTST, ���̺� - OM_ORD_EXP, �÷�- APLY_DLV_EXP, type- int(10), CHARSET- None, Ŀ��Ʈ- �����ۺ��, , IS_NULLABLE- NO
#Ÿ��: ELLTSETST, ���̺� - OM_ORD_EXP_OUT, �÷�- APLY_DLV_EXP, type- int(10), CHARSET- None, Ŀ��Ʈ- �����ۺ��, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_EXP_OUT CHANGE COLUMN `APLY_DLV_EXP` 
`APLY_DLV_EXP` int(10) NOT NULL 
comment '�����ۺ��';
#�ҽ�: ELLTOMTST, ���̺� - OM_ORD_EXP, �÷�- ACTL_PYF_DLV_EXP, type- int(11), CHARSET- None, Ŀ��Ʈ- �ǰ�����ۺ��, , IS_NULLABLE- NO
#Ÿ��: ELLTSETST, ���̺� - OM_ORD_EXP_OUT, �÷�- ACTL_PYF_DLV_EXP, type- int(11), CHARSET- None, Ŀ��Ʈ- �ǰ�����ۺ��, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_EXP_OUT CHANGE COLUMN `ACTL_PYF_DLV_EXP` 
`ACTL_PYF_DLV_EXP` int(11) NOT NULL 
comment '�ǰ�����ۺ��';
#�ҽ�: ELLTOMTST, ���̺� - OM_ORD_EXP, �÷�- EXP_FVR_AMT, type- int(10), CHARSET- None, Ŀ��Ʈ- ������ñݾ�, , IS_NULLABLE- NO
#Ÿ��: ELLTSETST, ���̺� - OM_ORD_EXP_OUT, �÷�- EXP_FVR_AMT, type- int(10), CHARSET- None, Ŀ��Ʈ- ������ñݾ�, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_EXP_OUT CHANGE COLUMN `EXP_FVR_AMT` 
`EXP_FVR_AMT` int(10) NOT NULL 
comment '������ñݾ�';
#�ҽ�: ELLTOMTST, ���̺� - OM_ORD_EXP, �÷�- CMPN_NO, type- varchar(8), CHARSET- utf8_general_ci, Ŀ��Ʈ- �����ι�ȣ, , IS_NULLABLE- YES
#Ÿ��: ELLTSETST, ���̺� - OM_ORD_EXP_OUT, �÷�- CMPN_NO, type- varchar(8), CHARSET- utf8_general_ci, Ŀ��Ʈ- ķ���ι�ȣ, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_EXP_OUT CHANGE COLUMN `CMPN_NO` 
`CMPN_NO` varchar(8)  NULL 
comment '�����ι�ȣ';

############ elltomtst.om_ord_exp -> elltombqtst.om_ord_exp_out##############

############ elltomtst.om_ord_fvr -> elltsetst.om_ord_fvr_out##############
#�ҽ�: ELLTOMTST, ���̺� - OM_ORD_FVR, �÷�- CMPN_ENTPRZ_SHARE_AMT, type- int(10), CHARSET- None, Ŀ��Ʈ- ķ���ξ�ü�д�ݾ�, , IS_NULLABLE- NO
#Ÿ��: ELLTSETST, ���̺� - OM_ORD_FVR_OUT, �÷�- CMPN_ENTPRZ_SHARE_AMT, type- int(10), CHARSET- None, Ŀ��Ʈ- ķ���ξ�ü�д�ݾ�, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_FVR_OUT CHANGE COLUMN `CMPN_ENTPRZ_SHARE_AMT` 
`CMPN_ENTPRZ_SHARE_AMT` int(10) NOT NULL 
comment 'ķ���ξ�ü�д�ݾ�';
#�ҽ�: ELLTOMTST, ���̺� - OM_ORD_FVR, �÷�- CMPN_ALYCO_SHARE_AMT, type- int(10), CHARSET- None, Ŀ��Ʈ- ķ�������޻�д�ݾ�, , IS_NULLABLE- NO
#Ÿ��: ELLTSETST, ���̺� - OM_ORD_FVR_OUT, �÷�- CMPN_ALYCO_SHARE_AMT, type- int(10), CHARSET- None, Ŀ��Ʈ- ķ�������޻�д�ݾ�, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_FVR_OUT CHANGE COLUMN `CMPN_ALYCO_SHARE_AMT` 
`CMPN_ALYCO_SHARE_AMT` int(10) NOT NULL 
comment 'ķ�������޻�д�ݾ�';
#�ҽ�: ELLTOMTST, ���̺� - OM_ORD_FVR, �÷�- FVR_UPRC, type- int(11), CHARSET- None, Ŀ��Ʈ- ���ôܰ�, , IS_NULLABLE- NO
#Ÿ��: ELLTSETST, ���̺� - OM_ORD_FVR_OUT, �÷�- FVR_UPRC, type- int(11), CHARSET- None, Ŀ��Ʈ- ���ôܰ�, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_FVR_OUT CHANGE COLUMN `FVR_UPRC` 
`FVR_UPRC` int(11) NOT NULL 
comment '���ôܰ�';
#�ҽ�: ELLTOMTST, ���̺� - OM_ORD_FVR, �÷�- ORD_SEQ, type- int(11), CHARSET- None, Ŀ��Ʈ- �ֹ�����, , IS_NULLABLE- NO
#Ÿ��: ELLTSETST, ���̺� - OM_ORD_FVR_OUT, �÷�- ORD_SEQ, type- int(11), CHARSET- None, Ŀ��Ʈ- �ֹ�����, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_FVR_OUT CHANGE COLUMN `ORD_SEQ` 
`ORD_SEQ` int(11) NOT NULL 
comment '�ֹ�����';

############ elltomtst.om_ord_fvr -> elltombqtst.om_ord_fvr_out##############

############ elltomtst.om_ord -> elltombqtst.om_ord_out##############

############ elltprtst.pr_cmpn_dc_goods_smry -> elltdptst.pr_cmpn_dc_goods_smry_out##############

############ elltprtst.pr_cmpn_dc_goods_smry -> elltgdtst.pr_cmpn_dc_goods_smry_out##############

############ elltprtst.pr_dc_xclud_goods -> elltdptst.pr_dc_xclud_goods_out##############

############ elltprtst.pr_dc_xclud_goods -> elltgdtst.pr_dc_xclud_goods_out##############

############ elltpytst.py_mbsh_point_if -> elltsetst.py_mbsh_point_if_out##############
#�ҽ�: ELLTPYTST, ���̺� - PY_MBSH_POINT_IF, �÷�- ORD_NO, type- varchar(30), CHARSET- utf8_general_ci, Ŀ��Ʈ- �ֹ���ȣ, , IS_NULLABLE- YES
#Ÿ��: ELLTSETST, ���̺� - PY_MBSH_POINT_IF_OUT, �÷�- ORD_NO, type- varchar(30), CHARSET- utf8_general_ci, Ŀ��Ʈ- �ֹ���ȣ, , IS_NULLABLE- NO
ALTER TABLE ELLTSETST.PY_MBSH_POINT_IF_OUT CHANGE COLUMN `ORD_NO` 
`ORD_NO` varchar(30)  NULL 
comment '�ֹ���ȣ';
#�ҽ�: ELLTPYTST, ���̺� - PY_MBSH_POINT_IF, �÷�- PYF_NO, type- int(11), CHARSET- None, Ŀ��Ʈ- ������ȣ, , IS_NULLABLE- YES
#Ÿ��: ELLTSETST, ���̺� - PY_MBSH_POINT_IF_OUT, �÷�- PYF_NO, type- int(11), CHARSET- None, Ŀ��Ʈ- ������ȣ, , IS_NULLABLE- NO
ALTER TABLE ELLTSETST.PY_MBSH_POINT_IF_OUT CHANGE COLUMN `PYF_NO` 
`PYF_NO` int(11)  NULL 
comment '������ȣ';
#PY_MBSH_POINT_IF_OUT:TRX_DVS_CD �÷� �ҽ��� ����
ALTER TABLE ELLTSETST.PY_MBSH_POINT_IF_OUT drop column `TRX_DVS_CD`;

############ elltpytst.py_pyf -> elltsetst.py_pyf_out##############
#�ҽ�: ELLTPYTST, ���̺� - PY_PYF, �÷�- PYF_PRCS_STAT_CD, type- varchar(20), CHARSET- utf8_general_ci, Ŀ��Ʈ- ����ó�������ڵ�
, , IS_NULLABLE- NO
#Ÿ��: ELLTSETST, ���̺� - PY_PYF_OUT, �÷�- PYF_PRCS_STAT_CD, type- varchar(20), CHARSET- utf8_general_ci, Ŀ��Ʈ- ����ó�������ڵ�
, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.PY_PYF_OUT CHANGE COLUMN `PYF_PRCS_STAT_CD` 
`PYF_PRCS_STAT_CD` varchar(20) NOT NULL 
comment '����ó�������ڵ�
';
#�ҽ�: ELLTPYTST, ���̺� - PY_PYF, �÷�- REFND_PSB_AMT, type- int(10), CHARSET- None, Ŀ��Ʈ- ȯ�Ұ��ɱݾ�, , IS_NULLABLE- NO
#Ÿ��: ELLTSETST, ���̺� - PY_PYF_OUT, �÷�- REFND_PSB_AMT, type- int(10), CHARSET- None, Ŀ��Ʈ- ȯ�Ұ��ɱݾ�, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.PY_PYF_OUT CHANGE COLUMN `REFND_PSB_AMT` 
`REFND_PSB_AMT` int(10) NOT NULL 
comment 'ȯ�Ұ��ɱݾ�';
#�ҽ�: ELLTPYTST, ���̺� - PY_PYF, �÷�- ORD_PRCS_STAT_CD, type- varchar(20), CHARSET- utf8_general_ci, Ŀ��Ʈ- �ֹ�ó�������ڵ�, , IS_NULLABLE- NO
#Ÿ��: ELLTSETST, ���̺� - PY_PYF_OUT, �÷�- ORD_PRCS_STAT_CD, type- varchar(20), CHARSET- utf8_general_ci, Ŀ��Ʈ- �ֹ�ó�������ڵ�, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.PY_PYF_OUT CHANGE COLUMN `ORD_PRCS_STAT_CD` 
`ORD_PRCS_STAT_CD` varchar(20) NOT NULL 
comment '�ֹ�ó�������ڵ�';
#�ҽ�: ELLTPYTST, ���̺� - PY_PYF, �÷�- MID, type- varchar(30), CHARSET- utf8_general_ci, Ŀ��Ʈ- MID, , IS_NULLABLE- YES
#Ÿ��: ELLTSETST, ���̺� - PY_PYF_OUT, �÷�- MID, type- int(11), CHARSET- None, Ŀ��Ʈ- MID, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.PY_PYF_OUT CHANGE COLUMN `MID` 
`MID` varchar(30)  NULL 
comment 'MID';

############ elltpytst.py_pyf -> elltombqtst.py_pyf_out##############

