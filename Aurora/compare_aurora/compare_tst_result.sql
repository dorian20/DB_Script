1. PRD
2. TEST
3. DEV
터널링포트 ellt1: 54423
터널링포트 ltcm1: 54425
터널링포트 ellt2: 54427
터널링포트 ellt3: 54429
터널링포트 ellt4: 54431
터널링포트 ellt5: 54433
터널링포트 ellt6: 54437
[('elltprtst', 'cc_intrst_mbr_dtl_out'), ('elltprtst', 'dp_dshop_dgoods_out'), ('elltprtst', 'dp_dshop_out'), ('ltcmattst', 'dp_scat_out'), ('elltlotst', 'et_entprz_hldy_out'), ('elltdptst', 'et_entshp_out'), ('elltprtst', 'et_entshp_out'), ('elltomtst', 'et_entshp_out'), ('elltomtst', 'et_entshp_owh_wtgval_out'), ('elltdptst', 'et_sup_entprz_out'), ('elltprtst', 'et_sup_entprz_out'), ('elltomtst', 'et_sup_entprz_owh_wtgval_out'), ('elltomtst', 'et_sup_entprz_prior_owh_out'), ('elltdptst', 'gd_brnd_conts_out'), ('elltdptst', 'gd_brnd_out'), ('elltprtst', 'gd_brnd_out'), ('elltcmtst', 'gd_brnd_out'), ('elltdptst', 'gd_goods_out'), ('ltcmattst', 'gd_goods_out'), ('elltprtst', 'gd_goods_out'), ('elltdptst', 'gd_goods_prc_out'), ('elltdptst', 'gd_goods_smry_out'), ('elltprtst', 'gd_goods_smry_out'), ('elltdptst', 'gd_item_sup_entprz_stk_out'), ('elltdptst', 'gd_md_gsgr_out'), ('elltprtst', 'gd_md_gsgr_out'), ('elltdptst', 'gd_sup_entprz_magn_out'), ('elltombqtst', 'lo_claim_dlv_out'), ('elltombqtst', 'lo_ord_dlv_out'), ('elltprtst', 'mb_ec_cust_out'), ('elltprtst', 'mb_mbr_grd_out'), ('elltsetst', 'om_claim_dtl_out'), ('elltombqtst', 'om_claim_dtl_out'), ('elltombqtst', 'om_claim_out'), ('elltsetst', 'om_ord_dtl_out'), ('elltombqtst', 'om_ord_dtl_out'), ('elltsetst', 'om_ord_exp_goods_out'), ('elltombqtst', 'om_ord_exp_goods_out'), ('elltsetst', 'om_ord_exp_out'), ('elltombqtst', 'om_ord_exp_out'), ('elltsetst', 'om_ord_fvr_out'), ('elltombqtst', 'om_ord_fvr_out'), ('elltombqtst', 'om_ord_out'), ('elltdptst', 'pr_cmpn_dc_goods_smry_out'), ('elltgdtst', 'pr_cmpn_dc_goods_smry_out'), ('elltdptst', 'pr_dc_xclud_goods_out'), ('elltgdtst', 'pr_dc_xclud_goods_out'), ('elltsetst', 'py_mbsh_point_if_out'), ('elltsetst', 'py_pyf_out'), ('elltombqtst', 'py_pyf_out')]
############ elltcctst.cc_intrst_mbr_dtl -> elltprtst.cc_intrst_mbr_dtl_out##############

############ elltdptst.dp_dshop_dgoods -> elltprtst.dp_dshop_dgoods_out##############

############ elltdptst.dp_dshop -> elltprtst.dp_dshop_out##############
#소스: ELLTDPTST, 테이블 - DP_DSHOP, 컬럼- RNKH_DSHOP_NO, type- int(5), CHARSET- None, 커맨트- 상위전시매장번호, , IS_NULLABLE- NO
#타겟: ELLTPRTST, 테이블 - DP_DSHOP_OUT, 컬럼- RNKH_DSHOP_NO, type- int(5), CHARSET- None, 커맨트- 상위전시매장번호, , IS_NULLABLE- YES
ALTER TABLE ELLTPRTST.DP_DSHOP_OUT CHANGE COLUMN `RNKH_DSHOP_NO` 
`RNKH_DSHOP_NO` int(5) NOT NULL 
comment '상위전시매장번호';

############ elltdptst.dp_scat -> ltcmattst.dp_scat_out##############

############ elltettst.et_entprz_hldy -> elltlotst.et_entprz_hldy_out##############
#소스: ELLTETTST, 테이블 - ET_ENTPRZ_HLDY, 컬럼- MODR_ID, type- varchar(30), CHARSET- utf8_general_ci, 커맨트- 수정자아이디, , IS_NULLABLE- NO
#타겟: ELLTLOTST, 테이블 - ET_ENTPRZ_HLDY_OUT, 컬럼- MODR_ID, type- varchar(30), CHARSET- utf8_general_ci, 커맨트- 수정자아이디, , IS_NULLABLE- YES
ALTER TABLE ELLTLOTST.ET_ENTPRZ_HLDY_OUT CHANGE COLUMN `MODR_ID` 
`MODR_ID` varchar(30) NOT NULL 
comment '수정자아이디';
#소스: ELLTETTST, 테이블 - ET_ENTPRZ_HLDY, 컬럼- MODI_DTTM, type- datetime, CHARSET- None, 커맨트- 수정일시, , IS_NULLABLE- NO
#타겟: ELLTLOTST, 테이블 - ET_ENTPRZ_HLDY_OUT, 컬럼- MODI_DTTM, type- datetime, CHARSET- None, 커맨트- 수정일시, , IS_NULLABLE- YES
ALTER TABLE ELLTLOTST.ET_ENTPRZ_HLDY_OUT CHANGE COLUMN `MODI_DTTM` 
`MODI_DTTM` datetime NOT NULL 
comment '수정일시';

############ elltettst.et_entshp -> elltdptst.et_entshp_out##############
#소스: ELLTETTST, 테이블 - ET_ENTSHP, 컬럼- HMPG_URL, type- varchar(150), CHARSET- utf8_general_ci, 커맨트- 홈페이지URL, , IS_NULLABLE- YES
#타겟: ELLTDPTST, 테이블 - ET_ENTSHP_OUT, 컬럼- HMPG_URL, type- varchar(150), CHARSET- ucs2_general_ci, 커맨트- , , IS_NULLABLE- YES
ALTER TABLE ELLTDPTST.ET_ENTSHP_OUT CHANGE COLUMN `HMPG_URL` 
`HMPG_URL` varchar(150)  NULL 
comment '홈페이지URL';
#소스: ELLTETTST, 테이블 - ET_ENTSHP, 컬럼- ENTSHP_GROUP_DVS_CD, type- varchar(20), CHARSET- utf8_general_ci, 커맨트- 입점그룹구분코드, , IS_NULLABLE- YES
#타겟: ELLTDPTST, 테이블 - ET_ENTSHP_OUT, 컬럼- ENTSHP_GROUP_DVS_CD, type- varchar(20), CHARSET- ucs2_general_ci, 커맨트- , , IS_NULLABLE- YES
ALTER TABLE ELLTDPTST.ET_ENTSHP_OUT CHANGE COLUMN `ENTSHP_GROUP_DVS_CD` 
`ENTSHP_GROUP_DVS_CD` varchar(20)  NULL 
comment '입점그룹구분코드';
#소스: ELLTETTST, 테이블 - ET_ENTSHP, 컬럼- ENTSHP_RGN_DVS_CD, type- varchar(20), CHARSET- utf8_general_ci, 커맨트- 입점지역구분코드, , IS_NULLABLE- YES
#타겟: ELLTDPTST, 테이블 - ET_ENTSHP_OUT, 컬럼- ENTSHP_RGN_DVS_CD, type- varchar(20), CHARSET- ucs2_general_ci, 커맨트- , , IS_NULLABLE- YES
ALTER TABLE ELLTDPTST.ET_ENTSHP_OUT CHANGE COLUMN `ENTSHP_RGN_DVS_CD` 
`ENTSHP_RGN_DVS_CD` varchar(20)  NULL 
comment '입점지역구분코드';
#소스: ELLTETTST, 테이블 - ET_ENTSHP, 컬럼- RGSTR_ID, type- varchar(30), CHARSET- utf8_general_ci, 커맨트- 등록자아이디, , IS_NULLABLE- NO
#타겟: ELLTDPTST, 테이블 - ET_ENTSHP_OUT, 컬럼- RGSTR_ID, type- varchar(30), CHARSET- ucs2_general_ci, 커맨트- , , IS_NULLABLE- YES
ALTER TABLE ELLTDPTST.ET_ENTSHP_OUT CHANGE COLUMN `RGSTR_ID` 
`RGSTR_ID` varchar(30) NOT NULL 
comment '등록자아이디';
#소스: ELLTETTST, 테이블 - ET_ENTSHP, 컬럼- RGSTR_NM, type- varchar(30), CHARSET- utf8_general_ci, 커맨트- 등록자명, , IS_NULLABLE- YES
#타겟: ELLTDPTST, 테이블 - ET_ENTSHP_OUT, 컬럼- RGSTR_NM, type- varchar(30), CHARSET- ucs2_general_ci, 커맨트- , , IS_NULLABLE- YES
ALTER TABLE ELLTDPTST.ET_ENTSHP_OUT CHANGE COLUMN `RGSTR_NM` 
`RGSTR_NM` varchar(30)  NULL 
comment '등록자명';
#소스: ELLTETTST, 테이블 - ET_ENTSHP, 컬럼- RGST_DTTM, type- datetime, CHARSET- None, 커맨트- 등록일시, , IS_NULLABLE- NO
#타겟: ELLTDPTST, 테이블 - ET_ENTSHP_OUT, 컬럼- RGST_DTTM, type- datetime, CHARSET- None, 커맨트- , , IS_NULLABLE- YES
ALTER TABLE ELLTDPTST.ET_ENTSHP_OUT CHANGE COLUMN `RGST_DTTM` 
`RGST_DTTM` datetime NOT NULL 
comment '등록일시';
#소스: ELLTETTST, 테이블 - ET_ENTSHP, 컬럼- MODR_ID, type- varchar(30), CHARSET- utf8_general_ci, 커맨트- 수정자아이디, , IS_NULLABLE- NO
#타겟: ELLTDPTST, 테이블 - ET_ENTSHP_OUT, 컬럼- MODR_ID, type- varchar(30), CHARSET- ucs2_general_ci, 커맨트- , , IS_NULLABLE- YES
ALTER TABLE ELLTDPTST.ET_ENTSHP_OUT CHANGE COLUMN `MODR_ID` 
`MODR_ID` varchar(30) NOT NULL 
comment '수정자아이디';
#소스: ELLTETTST, 테이블 - ET_ENTSHP, 컬럼- MODR_NM, type- varchar(30), CHARSET- utf8_general_ci, 커맨트- 수정자명, , IS_NULLABLE- YES
#타겟: ELLTDPTST, 테이블 - ET_ENTSHP_OUT, 컬럼- MODR_NM, type- varchar(30), CHARSET- ucs2_general_ci, 커맨트- , , IS_NULLABLE- YES
ALTER TABLE ELLTDPTST.ET_ENTSHP_OUT CHANGE COLUMN `MODR_NM` 
`MODR_NM` varchar(30)  NULL 
comment '수정자명';
#소스: ELLTETTST, 테이블 - ET_ENTSHP, 컬럼- MODI_DTTM, type- datetime, CHARSET- None, 커맨트- 수정일시, , IS_NULLABLE- NO
#타겟: ELLTDPTST, 테이블 - ET_ENTSHP_OUT, 컬럼- MODI_DTTM, type- datetime, CHARSET- None, 커맨트- , , IS_NULLABLE- YES
ALTER TABLE ELLTDPTST.ET_ENTSHP_OUT CHANGE COLUMN `MODI_DTTM` 
`MODI_DTTM` datetime NOT NULL 
comment '수정일시';

############ elltettst.et_entshp -> elltprtst.et_entshp_out##############

############ elltettst.et_entshp -> elltomtst.et_entshp_out##############

############ elltettst.et_entshp_owh_wtgval -> elltomtst.et_entshp_owh_wtgval_out##############

############ elltettst.et_sup_entprz -> elltdptst.et_sup_entprz_out##############
#소스: ELLTETTST, 테이블 - ET_SUP_ENTPRZ, 컬럼- RGSTR_NM, type- varchar(30), CHARSET- utf8_general_ci, 커맨트- 등록자명, , IS_NULLABLE- YES
#타겟: ELLTDPTST, 테이블 - ET_SUP_ENTPRZ_OUT, 컬럼- RGSTR_NM, type- varchar(30), CHARSET- ucs2_general_ci, 커맨트- , , IS_NULLABLE- YES
ALTER TABLE ELLTDPTST.ET_SUP_ENTPRZ_OUT CHANGE COLUMN `RGSTR_NM` 
`RGSTR_NM` varchar(30)  NULL 
comment '등록자명';
#소스: ELLTETTST, 테이블 - ET_SUP_ENTPRZ, 컬럼- MODR_NM, type- varchar(30), CHARSET- utf8_general_ci, 커맨트- 수정자명, , IS_NULLABLE- YES
#타겟: ELLTDPTST, 테이블 - ET_SUP_ENTPRZ_OUT, 컬럼- MODR_NM, type- varchar(30), CHARSET- ucs2_general_ci, 커맨트- , , IS_NULLABLE- YES
ALTER TABLE ELLTDPTST.ET_SUP_ENTPRZ_OUT CHANGE COLUMN `MODR_NM` 
`MODR_NM` varchar(30)  NULL 
comment '수정자명';

############ elltettst.et_sup_entprz -> elltprtst.et_sup_entprz_out##############

############ elltettst.et_sup_entprz_owh_wtgval -> elltomtst.et_sup_entprz_owh_wtgval_out##############

############ elltettst.et_sup_entprz_prior_owh -> elltomtst.et_sup_entprz_prior_owh_out##############

############ elltgdtst.gd_brnd_conts -> elltdptst.gd_brnd_conts_out##############
#소스: ELLTGDTST, 테이블 - GD_BRND_CONTS, 컬럼- BRND_NO, type- int(7), CHARSET- None, 커맨트- 브랜드번호, , IS_NULLABLE- NO
#타겟: ELLTDPTST, 테이블 - GD_BRND_CONTS_OUT, 컬럼- BRND_NO, type- int(10), CHARSET- None, 커맨트- 브랜드번호, , IS_NULLABLE- NO
ALTER TABLE ELLTDPTST.GD_BRND_CONTS_OUT CHANGE COLUMN `BRND_NO` 
`BRND_NO` int(7) NOT NULL 
comment '브랜드번호';

############ elltgdtst.gd_brnd -> elltdptst.gd_brnd_out##############
#소스: ELLTGDTST, 테이블 - GD_BRND, 컬럼- USE_YN, type- varchar(1), CHARSET- utf8_general_ci, 커맨트- 사용여부, , IS_NULLABLE- NO
#타겟: ELLTDPTST, 테이블 - GD_BRND_OUT, 컬럼- USE_YN, type- varchar(1), CHARSET- utf8_general_ci, 커맨트- , , IS_NULLABLE- NO
ALTER TABLE ELLTDPTST.GD_BRND_OUT CHANGE COLUMN `USE_YN` 
`USE_YN` varchar(1) NOT NULL 
comment '사용여부';

############ elltgdtst.gd_brnd -> elltprtst.gd_brnd_out##############

############ elltgdtst.gd_brnd -> elltcmtst.gd_brnd_out##############

############ elltgdtst.gd_goods -> elltdptst.gd_goods_out##############
#소스: ELLTGDTST, 테이블 - GD_GOODS, 컬럼- SL_STAT_CD, type- varchar(20), CHARSET- utf8_general_ci, 커맨트- 판매상태코드, , IS_NULLABLE- NO
#타겟: ELLTDPTST, 테이블 - GD_GOODS_OUT, 컬럼- SL_STAT_CD, type- varchar(20), CHARSET- utf8_general_ci, 커맨트- , , IS_NULLABLE- NO
ALTER TABLE ELLTDPTST.GD_GOODS_OUT CHANGE COLUMN `SL_STAT_CD` 
`SL_STAT_CD` varchar(20) NOT NULL 
comment '판매상태코드';

############ elltgdtst.gd_goods -> ltcmattst.gd_goods_out##############

############ elltgdtst.gd_goods -> elltprtst.gd_goods_out##############

############ elltgdtst.gd_goods_prc -> elltdptst.gd_goods_prc_out##############

############ elltgdtst.gd_goods_smry -> elltdptst.gd_goods_smry_out##############
#소스: ELLTGDTST, 테이블 - GD_GOODS_SMRY, 컬럼- CUST_STFD_EVLSCR1, type- smallint(2), CHARSET- None, 커맨트- 고객만족도평점1, , IS_NULLABLE- YES
#타겟: ELLTDPTST, 테이블 - GD_GOODS_SMRY_OUT, 컬럼- CUST_STFD_EVLSCR1, type- smallint(6), CHARSET- None, 커맨트- 고객만족도평점1, , IS_NULLABLE- YES
ALTER TABLE ELLTDPTST.GD_GOODS_SMRY_OUT CHANGE COLUMN `CUST_STFD_EVLSCR1` 
`CUST_STFD_EVLSCR1` smallint(2)  NULL 
comment '고객만족도평점1';
#소스: ELLTGDTST, 테이블 - GD_GOODS_SMRY, 컬럼- CUST_STFD_EVLSCR2, type- smallint(2), CHARSET- None, 커맨트- 고객만족도평점2, , IS_NULLABLE- YES
#타겟: ELLTDPTST, 테이블 - GD_GOODS_SMRY_OUT, 컬럼- CUST_STFD_EVLSCR2, type- smallint(6), CHARSET- None, 커맨트- 고객만족도평점2, , IS_NULLABLE- YES
ALTER TABLE ELLTDPTST.GD_GOODS_SMRY_OUT CHANGE COLUMN `CUST_STFD_EVLSCR2` 
`CUST_STFD_EVLSCR2` smallint(2)  NULL 
comment '고객만족도평점2';

############ elltgdtst.gd_goods_smry -> elltprtst.gd_goods_smry_out##############

############ elltgdtst.gd_item_sup_entprz_stk -> elltdptst.gd_item_sup_entprz_stk_out##############

############ elltgdtst.gd_md_gsgr -> elltdptst.gd_md_gsgr_out##############

############ elltgdtst.gd_md_gsgr -> elltprtst.gd_md_gsgr_out##############

############ elltgdtst.gd_sup_entprz_magn -> elltdptst.gd_sup_entprz_magn_out##############

############ elltlotst.lo_claim_dlv -> elltombqtst.lo_claim_dlv_out##############

############ elltlotst.lo_ord_dlv -> elltombqtst.lo_ord_dlv_out##############

############ elltmbtst.mb_ec_cust -> elltprtst.mb_ec_cust_out##############
#소스: ELLTMBTST, 테이블 - MB_EC_CUST, 컬럼- CUST_NM, type- varchar(30), CHARSET- utf8_general_ci, 커맨트- 고객명, , IS_NULLABLE- NO
#타겟: ELLTPRTST, 테이블 - MB_EC_CUST_OUT, 컬럼- CUST_NM, type- varchar(30), CHARSET- utf8_general_ci, 커맨트- 고객명, , IS_NULLABLE- YES
ALTER TABLE ELLTPRTST.MB_EC_CUST_OUT CHANGE COLUMN `CUST_NM` 
`CUST_NM` varchar(30) NOT NULL 
comment '고객명';
#소스: ELLTMBTST, 테이블 - MB_EC_CUST, 컬럼- MBR_LOGIN_ID, type- varchar(100), CHARSET- utf8_general_ci, 커맨트- 회원로그인아이디, , IS_NULLABLE- NO
#타겟: ELLTPRTST, 테이블 - MB_EC_CUST_OUT, 컬럼- MBR_LOGIN_ID, type- varchar(100), CHARSET- utf8_general_ci, 커맨트- 회원로그인아이디, , IS_NULLABLE- YES
ALTER TABLE ELLTPRTST.MB_EC_CUST_OUT CHANGE COLUMN `MBR_LOGIN_ID` 
`MBR_LOGIN_ID` varchar(100) NOT NULL 
comment '회원로그인아이디';
#MB_EC_CUST_OUT:MBR_GRADE_CD 컬럼 소스에 없음
ALTER TABLE ELLTPRTST.MB_EC_CUST_OUT drop column `MBR_GRADE_CD`;

############ elltmbtst.mb_mbr_grd -> elltprtst.mb_mbr_grd_out##############

############ elltomtst.om_claim_dtl -> elltsetst.om_claim_dtl_out##############
#소스: ELLTOMTST, 테이블 - OM_CLAIM_DTL, 컬럼- EXTRNL_IF_NO, type- int(11), CHARSET- None, 커맨트- 외부인터페이스번호, , IS_NULLABLE- NO
#타겟: ELLTSETST, 테이블 - OM_CLAIM_DTL_OUT, 컬럼- EXTRNL_IF_NO, type- int(11), CHARSET- None, 커맨트- 외부인터페이스번호, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_CLAIM_DTL_OUT CHANGE COLUMN `EXTRNL_IF_NO` 
`EXTRNL_IF_NO` int(11) NOT NULL 
comment '외부인터페이스번호';
#소스: ELLTOMTST, 테이블 - OM_CLAIM_DTL, 컬럼- CLAIM_DLVPLC_GROUP_NO, type- int(11), CHARSET- None, 커맨트- 클레임배송지그룹번호, , IS_NULLABLE- NO
#타겟: ELLTSETST, 테이블 - OM_CLAIM_DTL_OUT, 컬럼- CLAIM_DLVPLC_GROUP_NO, type- int(11), CHARSET- None, 커맨트- 클레임배송지그룹번호, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_CLAIM_DTL_OUT CHANGE COLUMN `CLAIM_DLVPLC_GROUP_NO` 
`CLAIM_DLVPLC_GROUP_NO` int(11) NOT NULL 
comment '클레임배송지그룹번호';

############ elltomtst.om_claim_dtl -> elltombqtst.om_claim_dtl_out##############

############ elltomtst.om_claim -> elltombqtst.om_claim_out##############

############ elltomtst.om_ord_dtl -> elltsetst.om_ord_dtl_out##############
#소스: ELLTOMTST, 테이블 - OM_ORD_DTL, 컬럼- EXTRNL_IF_NO, type- int(11), CHARSET- None, 커맨트- 외부인터페이스번호, , IS_NULLABLE- NO
#타겟: ELLTSETST, 테이블 - OM_ORD_DTL_OUT, 컬럼- EXTRNL_IF_NO, type- int(11), CHARSET- None, 커맨트- 외부인터페이스번호, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_DTL_OUT CHANGE COLUMN `EXTRNL_IF_NO` 
`EXTRNL_IF_NO` int(11) NOT NULL 
comment '외부인터페이스번호';
#소스: ELLTOMTST, 테이블 - OM_ORD_DTL, 컬럼- ORD_DLVPLC_GROUP_NO, type- int(11), CHARSET- None, 커맨트- 주문배송지그룹번호, , IS_NULLABLE- NO
#타겟: ELLTSETST, 테이블 - OM_ORD_DTL_OUT, 컬럼- ORD_DLVPLC_GROUP_NO, type- int(11), CHARSET- None, 커맨트- 주문배송지그룹번호, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_DTL_OUT CHANGE COLUMN `ORD_DLVPLC_GROUP_NO` 
`ORD_DLVPLC_GROUP_NO` int(11) NOT NULL 
comment '주문배송지그룹번호';
#소스: ELLTOMTST, 테이블 - OM_ORD_DTL, 컬럼- ORD_EXP_GROUP_NO, type- int(4), CHARSET- None, 커맨트- 주문비용그룹번호, , IS_NULLABLE- NO
#타겟: ELLTSETST, 테이블 - OM_ORD_DTL_OUT, 컬럼- ORD_EXP_GROUP_NO, type- int(4), CHARSET- None, 커맨트- 주문비용그룹번호, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_DTL_OUT CHANGE COLUMN `ORD_EXP_GROUP_NO` 
`ORD_EXP_GROUP_NO` int(4) NOT NULL 
comment '주문비용그룹번호';
#소스: ELLTOMTST, 테이블 - OM_ORD_DTL, 컬럼- ORD_ALTMNT_GROUP_NO, type- smallint(6), CHARSET- None, 커맨트- 주문배분그룹번호, , IS_NULLABLE- NO
#타겟: ELLTSETST, 테이블 - OM_ORD_DTL_OUT, 컬럼- ORD_ALTMNT_GROUP_NO, type- smallint(6), CHARSET- None, 커맨트- 주문배분그룹번호, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_DTL_OUT CHANGE COLUMN `ORD_ALTMNT_GROUP_NO` 
`ORD_ALTMNT_GROUP_NO` smallint(6) NOT NULL 
comment '주문배분그룹번호';
#소스: ELLTOMTST, 테이블 - OM_ORD_DTL, 컬럼- SLPRC, type- int(10), CHARSET- None, 커맨트- 판매가, , IS_NULLABLE- NO
#타겟: ELLTSETST, 테이블 - OM_ORD_DTL_OUT, 컬럼- SLPRC, type- int(11), CHARSET- None, 커맨트- 판매가, , IS_NULLABLE- NO
ALTER TABLE ELLTSETST.OM_ORD_DTL_OUT CHANGE COLUMN `SLPRC` 
`SLPRC` int(10) NOT NULL 
comment '판매가';
#소스: ELLTOMTST, 테이블 - OM_ORD_DTL, 컬럼- STRPIC_LOC_CD, type- varchar(20), CHARSET- utf8_general_ci, 커맨트- 스마트위치코드, , IS_NULLABLE- YES
#타겟: ELLTSETST, 테이블 - OM_ORD_DTL_OUT, 컬럼- STRPIC_LOC_CD, type- varchar(20), CHARSET- utf8_general_ci, 커맨트- 스마트픽위치코드, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_DTL_OUT CHANGE COLUMN `STRPIC_LOC_CD` 
`STRPIC_LOC_CD` varchar(20)  NULL 
comment '스마트위치코드';

############ elltomtst.om_ord_dtl -> elltombqtst.om_ord_dtl_out##############

############ elltomtst.om_ord_exp_goods -> elltsetst.om_ord_exp_goods_out##############
#소스: ELLTOMTST, 테이블 - OM_ORD_EXP_GOODS, 컬럼- ORD_SEQ, type- int(11), CHARSET- None, 커맨트- 주문순번, , IS_NULLABLE- NO
#타겟: ELLTSETST, 테이블 - OM_ORD_EXP_GOODS_OUT, 컬럼- ORD_SEQ, type- int(11), CHARSET- None, 커맨트- 주문순번, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_EXP_GOODS_OUT CHANGE COLUMN `ORD_SEQ` 
`ORD_SEQ` int(11) NOT NULL 
comment '주문순번';

############ elltomtst.om_ord_exp_goods -> elltombqtst.om_ord_exp_goods_out##############

############ elltomtst.om_ord_exp -> elltsetst.om_ord_exp_out##############
#소스: ELLTOMTST, 테이블 - OM_ORD_EXP, 컬럼- DLV_EXP, type- int(10), CHARSET- None, 커맨트- 배송비용, , IS_NULLABLE- NO
#타겟: ELLTSETST, 테이블 - OM_ORD_EXP_OUT, 컬럼- DLV_EXP, type- int(10), CHARSET- None, 커맨트- 배송비용, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_EXP_OUT CHANGE COLUMN `DLV_EXP` 
`DLV_EXP` int(10) NOT NULL 
comment '배송비용';
#소스: ELLTOMTST, 테이블 - OM_ORD_EXP, 컬럼- STD_AMT, type- int(11), CHARSET- None, 커맨트- 기준금액, , IS_NULLABLE- NO
#타겟: ELLTSETST, 테이블 - OM_ORD_EXP_OUT, 컬럼- STD_AMT, type- int(11), CHARSET- None, 커맨트- 기준금액, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_EXP_OUT CHANGE COLUMN `STD_AMT` 
`STD_AMT` int(11) NOT NULL 
comment '기준금액';
#소스: ELLTOMTST, 테이블 - OM_ORD_EXP, 컬럼- RTN_EXP, type- int(10), CHARSET- None, 커맨트- 반품비용, , IS_NULLABLE- NO
#타겟: ELLTSETST, 테이블 - OM_ORD_EXP_OUT, 컬럼- RTN_EXP, type- int(10), CHARSET- None, 커맨트- 반품비용, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_EXP_OUT CHANGE COLUMN `RTN_EXP` 
`RTN_EXP` int(10) NOT NULL 
comment '반품비용';
#소스: ELLTOMTST, 테이블 - OM_ORD_EXP, 컬럼- APLY_DLV_EXP, type- int(10), CHARSET- None, 커맨트- 적용배송비용, , IS_NULLABLE- NO
#타겟: ELLTSETST, 테이블 - OM_ORD_EXP_OUT, 컬럼- APLY_DLV_EXP, type- int(10), CHARSET- None, 커맨트- 적용배송비용, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_EXP_OUT CHANGE COLUMN `APLY_DLV_EXP` 
`APLY_DLV_EXP` int(10) NOT NULL 
comment '적용배송비용';
#소스: ELLTOMTST, 테이블 - OM_ORD_EXP, 컬럼- ACTL_PYF_DLV_EXP, type- int(11), CHARSET- None, 커맨트- 실결제배송비용, , IS_NULLABLE- NO
#타겟: ELLTSETST, 테이블 - OM_ORD_EXP_OUT, 컬럼- ACTL_PYF_DLV_EXP, type- int(11), CHARSET- None, 커맨트- 실결제배송비용, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_EXP_OUT CHANGE COLUMN `ACTL_PYF_DLV_EXP` 
`ACTL_PYF_DLV_EXP` int(11) NOT NULL 
comment '실결제배송비용';
#소스: ELLTOMTST, 테이블 - OM_ORD_EXP, 컬럼- EXP_FVR_AMT, type- int(10), CHARSET- None, 커맨트- 비용혜택금액, , IS_NULLABLE- NO
#타겟: ELLTSETST, 테이블 - OM_ORD_EXP_OUT, 컬럼- EXP_FVR_AMT, type- int(10), CHARSET- None, 커맨트- 비용혜택금액, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_EXP_OUT CHANGE COLUMN `EXP_FVR_AMT` 
`EXP_FVR_AMT` int(10) NOT NULL 
comment '비용혜택금액';
#소스: ELLTOMTST, 테이블 - OM_ORD_EXP, 컬럼- CMPN_NO, type- varchar(8), CHARSET- utf8_general_ci, 커맨트- 켐페인번호, , IS_NULLABLE- YES
#타겟: ELLTSETST, 테이블 - OM_ORD_EXP_OUT, 컬럼- CMPN_NO, type- varchar(8), CHARSET- utf8_general_ci, 커맨트- 캠페인번호, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_EXP_OUT CHANGE COLUMN `CMPN_NO` 
`CMPN_NO` varchar(8)  NULL 
comment '켐페인번호';

############ elltomtst.om_ord_exp -> elltombqtst.om_ord_exp_out##############

############ elltomtst.om_ord_fvr -> elltsetst.om_ord_fvr_out##############
#소스: ELLTOMTST, 테이블 - OM_ORD_FVR, 컬럼- CMPN_ENTPRZ_SHARE_AMT, type- int(10), CHARSET- None, 커맨트- 캠페인업체분담금액, , IS_NULLABLE- NO
#타겟: ELLTSETST, 테이블 - OM_ORD_FVR_OUT, 컬럼- CMPN_ENTPRZ_SHARE_AMT, type- int(10), CHARSET- None, 커맨트- 캠페인업체분담금액, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_FVR_OUT CHANGE COLUMN `CMPN_ENTPRZ_SHARE_AMT` 
`CMPN_ENTPRZ_SHARE_AMT` int(10) NOT NULL 
comment '캠페인업체분담금액';
#소스: ELLTOMTST, 테이블 - OM_ORD_FVR, 컬럼- CMPN_ALYCO_SHARE_AMT, type- int(10), CHARSET- None, 커맨트- 캠페인제휴사분담금액, , IS_NULLABLE- NO
#타겟: ELLTSETST, 테이블 - OM_ORD_FVR_OUT, 컬럼- CMPN_ALYCO_SHARE_AMT, type- int(10), CHARSET- None, 커맨트- 캠페인제휴사분담금액, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_FVR_OUT CHANGE COLUMN `CMPN_ALYCO_SHARE_AMT` 
`CMPN_ALYCO_SHARE_AMT` int(10) NOT NULL 
comment '캠페인제휴사분담금액';
#소스: ELLTOMTST, 테이블 - OM_ORD_FVR, 컬럼- FVR_UPRC, type- int(11), CHARSET- None, 커맨트- 혜택단가, , IS_NULLABLE- NO
#타겟: ELLTSETST, 테이블 - OM_ORD_FVR_OUT, 컬럼- FVR_UPRC, type- int(11), CHARSET- None, 커맨트- 혜택단가, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_FVR_OUT CHANGE COLUMN `FVR_UPRC` 
`FVR_UPRC` int(11) NOT NULL 
comment '혜택단가';
#소스: ELLTOMTST, 테이블 - OM_ORD_FVR, 컬럼- ORD_SEQ, type- int(11), CHARSET- None, 커맨트- 주문순번, , IS_NULLABLE- NO
#타겟: ELLTSETST, 테이블 - OM_ORD_FVR_OUT, 컬럼- ORD_SEQ, type- int(11), CHARSET- None, 커맨트- 주문순번, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.OM_ORD_FVR_OUT CHANGE COLUMN `ORD_SEQ` 
`ORD_SEQ` int(11) NOT NULL 
comment '주문순번';

############ elltomtst.om_ord_fvr -> elltombqtst.om_ord_fvr_out##############

############ elltomtst.om_ord -> elltombqtst.om_ord_out##############

############ elltprtst.pr_cmpn_dc_goods_smry -> elltdptst.pr_cmpn_dc_goods_smry_out##############

############ elltprtst.pr_cmpn_dc_goods_smry -> elltgdtst.pr_cmpn_dc_goods_smry_out##############

############ elltprtst.pr_dc_xclud_goods -> elltdptst.pr_dc_xclud_goods_out##############

############ elltprtst.pr_dc_xclud_goods -> elltgdtst.pr_dc_xclud_goods_out##############

############ elltpytst.py_mbsh_point_if -> elltsetst.py_mbsh_point_if_out##############
#소스: ELLTPYTST, 테이블 - PY_MBSH_POINT_IF, 컬럼- ORD_NO, type- varchar(30), CHARSET- utf8_general_ci, 커맨트- 주문번호, , IS_NULLABLE- YES
#타겟: ELLTSETST, 테이블 - PY_MBSH_POINT_IF_OUT, 컬럼- ORD_NO, type- varchar(30), CHARSET- utf8_general_ci, 커맨트- 주문번호, , IS_NULLABLE- NO
ALTER TABLE ELLTSETST.PY_MBSH_POINT_IF_OUT CHANGE COLUMN `ORD_NO` 
`ORD_NO` varchar(30)  NULL 
comment '주문번호';
#소스: ELLTPYTST, 테이블 - PY_MBSH_POINT_IF, 컬럼- PYF_NO, type- int(11), CHARSET- None, 커맨트- 결제번호, , IS_NULLABLE- YES
#타겟: ELLTSETST, 테이블 - PY_MBSH_POINT_IF_OUT, 컬럼- PYF_NO, type- int(11), CHARSET- None, 커맨트- 결제번호, , IS_NULLABLE- NO
ALTER TABLE ELLTSETST.PY_MBSH_POINT_IF_OUT CHANGE COLUMN `PYF_NO` 
`PYF_NO` int(11)  NULL 
comment '결제번호';
#PY_MBSH_POINT_IF_OUT:TRX_DVS_CD 컬럼 소스에 없음
ALTER TABLE ELLTSETST.PY_MBSH_POINT_IF_OUT drop column `TRX_DVS_CD`;

############ elltpytst.py_pyf -> elltsetst.py_pyf_out##############
#소스: ELLTPYTST, 테이블 - PY_PYF, 컬럼- PYF_PRCS_STAT_CD, type- varchar(20), CHARSET- utf8_general_ci, 커맨트- 결제처리상태코드
, , IS_NULLABLE- NO
#타겟: ELLTSETST, 테이블 - PY_PYF_OUT, 컬럼- PYF_PRCS_STAT_CD, type- varchar(20), CHARSET- utf8_general_ci, 커맨트- 결제처리상태코드
, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.PY_PYF_OUT CHANGE COLUMN `PYF_PRCS_STAT_CD` 
`PYF_PRCS_STAT_CD` varchar(20) NOT NULL 
comment '결제처리상태코드
';
#소스: ELLTPYTST, 테이블 - PY_PYF, 컬럼- REFND_PSB_AMT, type- int(10), CHARSET- None, 커맨트- 환불가능금액, , IS_NULLABLE- NO
#타겟: ELLTSETST, 테이블 - PY_PYF_OUT, 컬럼- REFND_PSB_AMT, type- int(10), CHARSET- None, 커맨트- 환불가능금액, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.PY_PYF_OUT CHANGE COLUMN `REFND_PSB_AMT` 
`REFND_PSB_AMT` int(10) NOT NULL 
comment '환불가능금액';
#소스: ELLTPYTST, 테이블 - PY_PYF, 컬럼- ORD_PRCS_STAT_CD, type- varchar(20), CHARSET- utf8_general_ci, 커맨트- 주문처리상태코드, , IS_NULLABLE- NO
#타겟: ELLTSETST, 테이블 - PY_PYF_OUT, 컬럼- ORD_PRCS_STAT_CD, type- varchar(20), CHARSET- utf8_general_ci, 커맨트- 주문처리상태코드, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.PY_PYF_OUT CHANGE COLUMN `ORD_PRCS_STAT_CD` 
`ORD_PRCS_STAT_CD` varchar(20) NOT NULL 
comment '주문처리상태코드';
#소스: ELLTPYTST, 테이블 - PY_PYF, 컬럼- MID, type- varchar(30), CHARSET- utf8_general_ci, 커맨트- MID, , IS_NULLABLE- YES
#타겟: ELLTSETST, 테이블 - PY_PYF_OUT, 컬럼- MID, type- int(11), CHARSET- None, 커맨트- MID, , IS_NULLABLE- YES
ALTER TABLE ELLTSETST.PY_PYF_OUT CHANGE COLUMN `MID` 
`MID` varchar(30)  NULL 
comment 'MID';

############ elltpytst.py_pyf -> elltombqtst.py_pyf_out##############

