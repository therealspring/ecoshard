"""Download rasters and style files for IPBES Paper."""
import os
import subprocess

RASTER_URL_LIST = [
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/nutrient_NC_10s_cur_compressed_md5_750e58205efb24f29fb88ec282eb0143.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/nutrient_NC_10s_ssp1_md5_9b2be93d642f895d7b847765a5072737.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/nutrient_NC_10s_ssp3_md5_7b018804dd2c60367fec1a2b34a6f9e3.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/nutrient_NC_10s_ssp5_md5_0efb0f2cae142033a9f016f6b33b8a3f.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/nutrient_NC_change_10s_ssp1_compressed_md5_1ab5bd72043041dc3c46874d870141c4.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/nutrient_NC_change_10s_ssp3_compressed_md5_63e2f488dd718e5e0e4801dfb6dc0d00.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/nutrient_NC_change_10s_ssp5_compressed_md5_1b0a700d4d150a5e6bd76d87f14ab538.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/nutrient_deficit_10s_cur_compressed_md5_031d4bb444325835315a2cc825be3fd4.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/nutrient_deficit_10s_ssp1_md5_136b1b2609481749ed963fd6bc61a240.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/nutrient_deficit_10s_ssp3_md5_93c3df4e358dcde8054426ffcad4b4fe.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/nutrient_deficit_10s_ssp5_md5_7a23f76129d0f3b6aa1987d534a0960e.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/nutrient_deficit_change_10s_ssp1_compressed_md5_fbeb8122b920cf13c325284baeba640c.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/nutrient_deficit_change_10s_ssp3_compressed_md5_6a2352b77f23421c1a48711a3e1d703a.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/nutrient_deficit_change_10s_ssp5_compressed_md5_1244e34777bb5c0980e263390b10d6d0.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/nutrient_pop_30s_cur_compressed_md5_a728d722935371a17452276ba1034296.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/nutrient_pop_30s_ssp1_md5_83f3043b257de97168c51adcd9f0006c.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/nutrient_pop_30s_ssp3_md5_c64398ed9a8329b2979e209b631afddb.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/nutrient_pop_30s_ssp5_md5_a35c2fc540b3bd5f0e55201020d52224.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/nutrient_pop_change_30s_ssp1_compressed_md5_fdadefe1e84c5dcc83e76dd7cb4f1564.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/nutrient_pop_change_30s_ssp3_compressed_md5_2d886ae99fc3241c05398a8948bf0f3a.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/nutrient_pop_change_30s_ssp5_compressed_md5_72a80daaaecf1480069dfb031d4eea12.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/nutrient_potential_10s_cur_compressed_md5_9e0ae4df4e399350087c1c2d00d0a1bb.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/nutrient_potential_10s_ssp1_md5_043459977567bfc837ad4208c4f90f16.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/nutrient_potential_10s_ssp3_md5_ad4decd02bec2205bf9073f075c5bda9.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/nutrient_potential_10s_ssp5_md5_3f63cebb84fa2acce1019e66e13dfb49.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/nutrient_potential_change_10s_ssp1_compressed_md5_6a5228b9630642437a12a436be4ebe41.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/nutrient_potential_change_10s_ssp3_compressed_md5_06e7e47952d6b1ec5bc784737b7989ac.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/nutrient_potential_change_10s_ssp5_compressed_md5_1d6eb591625a6563bb64c06cf0f2a5a9.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/pollination_NC_10s_cur_compressed_md5_5bea8fbf1d97ef6c2b539c97887e05a0.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/pollination_NC_change_10s_ssp1_compressed_md5_b731503ebc5f7e484c8935dcce6ba79c.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/pollination_NC_change_10s_ssp3_compressed_md5_613532434a7e247e9c09a542bf853e5e.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/pollination_NC_change_10s_ssp5_compressed_md5_099d2aaec6051be39b9cffb91fcb1260.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/pollination_deficit_10s_cur_compressed_md5_6db2748b01d6541663f0698a8f34a607.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/pollination_deficit_change_10s_ssp1_compressed_md5_7b743214d92a37712f1fa678427f95ad.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/pollination_deficit_change_10s_ssp3_compressed_md5_5a0488cac7fd542066c4b36596c67f36.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/pollination_deficit_change_10s_ssp5_compressed_md5_19f1e1f027e468ea2217903c605cd0b7.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/pollination_potential_10s_cur_compressed_md5_20e27265b1627b6fbdb10b5fa504e745.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/pollination_potential_abschange_10s_ssp1_md5_da5f61b9001adb2c5ba1a795718a9f90.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/pollination_potential_abschange_10s_ssp3_md5_6309f3eedab1bde1279ce3e1560a935d.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/pollination_potential_abschange_10s_ssp5_md5_99bf4ab9c9e93d7b7da96428062eadbc.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/pollination_NC_10s_ssp1_md5_4d307c30e932af67d98e40f7c5d74982.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/pollination_NC_10s_ssp3_md5_9b5af8879fd2cfdceb7485009397ebcd.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/pollination_NC_10s_ssp5_md5_561bbf17dae9d13e28ce78cb8feb32c6.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/pollination_deficit_10s_ssp1_md5_67458bc3a7eae87a02a072a8f16ff138.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/pollination_deficit_10s_ssp3_md5_22f75fb4de30195f93c49b3a3375d7f7.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/pollination_deficit_10s_ssp5_md5_37892e314197054e7b8eb87a16b4427d.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/pollination_pop_30s_cur_md5_566d70b81ef5a1746ab5c66cbbe1d658.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/pollination_pop_30s_ssp1_md5_6396d2fd1400feb58f645d853b52ac85.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/pollination_pop_30s_ssp3_md5_b49a597d072d305834bfd1b6992a7b76.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/pollination_pop_30s_ssp5_md5_858ebf9569faba854e880443baa40c68.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/pollination_pop_change_30s_ssp1_md5_353845ac0bdc57ce67af15ae2bd9c593.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/pollination_pop_change_30s_ssp3_md5_0e58c680d510edcb20d2118eff3a47bd.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/pollination_pop_change_30s_ssp5_md5_670ab322ab9deb6820b5e16749377204.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/pollination_potential_10s_ssp1_md5_57c03ee9393878d56eb7d896ab20b47a.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/pollination_potential_10s_ssp3_md5_f785e47f2a70f98b5d9deb251c42d9f5.tif',
    'https://storage.googleapis.com/ipbes-natcap-ecoshard-data-for-publication/pollination_potential_10s_ssp5_md5_4b06474ca808725f49fbaca3fee4fe85.tif',
]

STYLE_URL_LIST = [
    'https://drive.google.com/uc?export=download&id=1gLvZe_u3R31fuTc91H3XwpF0vvAb1m-Q',
    'https://drive.google.com/uc?export=download&id=1gLvZe_u3R31fuTc91H3XwpF0vvAb1m-Q',
    'https://drive.google.com/uc?export=download&id=1gLvZe_u3R31fuTc91H3XwpF0vvAb1m-Q',
    'https://drive.google.com/uc?export=download&id=1gLvZe_u3R31fuTc91H3XwpF0vvAb1m-Q',
    'https://drive.google.com/uc?export=download&id=13AD6Ecb_dP3cnOWqEf4qBS8EAsalSQrj',
    'https://drive.google.com/uc?export=download&id=13AD6Ecb_dP3cnOWqEf4qBS8EAsalSQrj',
    'https://drive.google.com/uc?export=download&id=13AD6Ecb_dP3cnOWqEf4qBS8EAsalSQrj',
    'https://drive.google.com/uc?export=download&id=1-rs2XT0n4KkiiQO2eNxA-eoukGT5oBqj',
    'https://drive.google.com/uc?export=download&id=1-rs2XT0n4KkiiQO2eNxA-eoukGT5oBqj',
    'https://drive.google.com/uc?export=download&id=1-rs2XT0n4KkiiQO2eNxA-eoukGT5oBqj',
    'https://drive.google.com/uc?export=download&id=1-rs2XT0n4KkiiQO2eNxA-eoukGT5oBqj',
    'https://drive.google.com/uc?export=download&id=1fm-0eGCLhF6YAQINjPWMIFmSGz1ehpL7',
    'https://drive.google.com/uc?export=download&id=1fm-0eGCLhF6YAQINjPWMIFmSGz1ehpL7',
    'https://drive.google.com/uc?export=download&id=1fm-0eGCLhF6YAQINjPWMIFmSGz1ehpL7',
    'https://drive.google.com/uc?export=download&id=1IUaVxt-59YieFb83d0q1DkOFBezmB_1h',
    'https://drive.google.com/uc?export=download&id=1IUaVxt-59YieFb83d0q1DkOFBezmB_1h',
    'https://drive.google.com/uc?export=download&id=1IUaVxt-59YieFb83d0q1DkOFBezmB_1h',
    'https://drive.google.com/uc?export=download&id=1IUaVxt-59YieFb83d0q1DkOFBezmB_1h',
    'https://drive.google.com/uc?export=download&id=1fm-0eGCLhF6YAQINjPWMIFmSGz1ehpL7',
    'https://drive.google.com/uc?export=download&id=1fm-0eGCLhF6YAQINjPWMIFmSGz1ehpL7',
    'https://drive.google.com/uc?export=download&id=1fm-0eGCLhF6YAQINjPWMIFmSGz1ehpL7',
    'https://drive.google.com/uc?export=download&id=1-rs2XT0n4KkiiQO2eNxA-eoukGT5oBqj',
    'https://drive.google.com/uc?export=download&id=1-rs2XT0n4KkiiQO2eNxA-eoukGT5oBqj',
    'https://drive.google.com/uc?export=download&id=1-rs2XT0n4KkiiQO2eNxA-eoukGT5oBqj',
    'https://drive.google.com/uc?export=download&id=1-rs2XT0n4KkiiQO2eNxA-eoukGT5oBqj',
    'https://drive.google.com/uc?export=download&id=1fm-0eGCLhF6YAQINjPWMIFmSGz1ehpL7',
    'https://drive.google.com/uc?export=download&id=1fm-0eGCLhF6YAQINjPWMIFmSGz1ehpL7',
    'https://drive.google.com/uc?export=download&id=1fm-0eGCLhF6YAQINjPWMIFmSGz1ehpL7',
    'https://drive.google.com/uc?export=download&id=1gLvZe_u3R31fuTc91H3XwpF0vvAb1m-Q',
    'https://drive.google.com/uc?export=download&id=13AD6Ecb_dP3cnOWqEf4qBS8EAsalSQrj',
    'https://drive.google.com/uc?export=download&id=13AD6Ecb_dP3cnOWqEf4qBS8EAsalSQrj',
    'https://drive.google.com/uc?export=download&id=13AD6Ecb_dP3cnOWqEf4qBS8EAsalSQrj',
    'https://drive.google.com/uc?export=download&id=1-rs2XT0n4KkiiQO2eNxA-eoukGT5oBqj',
    'https://drive.google.com/uc?export=download&id=1fm-0eGCLhF6YAQINjPWMIFmSGz1ehpL7',
    'https://drive.google.com/uc?export=download&id=1fm-0eGCLhF6YAQINjPWMIFmSGz1ehpL7',
    'https://drive.google.com/uc?export=download&id=1fm-0eGCLhF6YAQINjPWMIFmSGz1ehpL7',
    'https://drive.google.com/uc?export=download&id=1-rs2XT0n4KkiiQO2eNxA-eoukGT5oBqj',
    'https://drive.google.com/uc?export=download&id=1zwnCMsWMPJBAC4EuuJiSNvdl4AM8OA5W',
    'https://drive.google.com/uc?export=download&id=1zwnCMsWMPJBAC4EuuJiSNvdl4AM8OA5W',
    'https://drive.google.com/uc?export=download&id=1zwnCMsWMPJBAC4EuuJiSNvdl4AM8OA5W',
    'https://drive.google.com/uc?export=download&id=1gLvZe_u3R31fuTc91H3XwpF0vvAb1m-Q',
    'https://drive.google.com/uc?export=download&id=1gLvZe_u3R31fuTc91H3XwpF0vvAb1m-Q',
    'https://drive.google.com/uc?export=download&id=1gLvZe_u3R31fuTc91H3XwpF0vvAb1m-Q',
    'https://drive.google.com/uc?export=download&id=1-rs2XT0n4KkiiQO2eNxA-eoukGT5oBqj',
    'https://drive.google.com/uc?export=download&id=1-rs2XT0n4KkiiQO2eNxA-eoukGT5oBqj',
    'https://drive.google.com/uc?export=download&id=1-rs2XT0n4KkiiQO2eNxA-eoukGT5oBqj',
    'https://drive.google.com/uc?export=download&id=1ZfTqGX8LGpX-pNXOOVjTHmen2BE7MMnm',
    'https://drive.google.com/uc?export=download&id=1ZfTqGX8LGpX-pNXOOVjTHmen2BE7MMnm',
    'https://drive.google.com/uc?export=download&id=1ZfTqGX8LGpX-pNXOOVjTHmen2BE7MMnm',
    'https://drive.google.com/uc?export=download&id=1ZfTqGX8LGpX-pNXOOVjTHmen2BE7MMnm',
    'https://drive.google.com/uc?export=download&id=1fm-0eGCLhF6YAQINjPWMIFmSGz1ehpL7',
    'https://drive.google.com/uc?export=download&id=1fm-0eGCLhF6YAQINjPWMIFmSGz1ehpL7',
    'https://drive.google.com/uc?export=download&id=1fm-0eGCLhF6YAQINjPWMIFmSGz1ehpL7',
    'https://drive.google.com/uc?export=download&id=1-rs2XT0n4KkiiQO2eNxA-eoukGT5oBqj',
    'https://drive.google.com/uc?export=download&id=1-rs2XT0n4KkiiQO2eNxA-eoukGT5oBqj',
    'https://drive.google.com/uc?export=download&id=1-rs2XT0n4KkiiQO2eNxA-eoukGT5oBqj'
]

if __name__ == '__main__':
    for raster_url, style_url in zip(RASTER_URL_LIST, STYLE_URL_LIST):
        target_raster_path = os.path.basename(raster_url)
        subprocess.run('curl -L -o %s %s' % (target_raster_path, raster_url), shell=True)
        target_style_path = '%s.qml ' % (
            os.path.splitext(target_raster_path)[0])
        subprocess.run('curl -L -o %s %s' % (target_style_path, style_url), shell=True)