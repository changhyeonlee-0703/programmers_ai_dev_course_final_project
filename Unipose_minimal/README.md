# Unipose_minimal
<p align="justify">
  <strong>HMM 습관 인증 Pre-Trained weights</strong> / 
  <a href="https://github.com/programmersA4/UniPose_minimal/releases/">Release Draft</a>
  / 
  <a href="https://github.com/programmersA4/Unipose_minimal/releases/download/untagged-96faa91c1481761ff602/UniPose_COCO.pth">다운로드 링크</a>
</p>
<br/>
<br/>


<hr/>

## Unipose (original)

<br/>

<p>
<a href=https://github.com/bmartacho/UniPose><strong>https://github.com/bmartacho/UniPose</strong><a/>

  <a href="https://openaccess.thecvf.com/content_CVPR_2020/html/Artacho_UniPose_Unified_Human_Pose_Estimation_in_Single_Images_and_Videos_CVPR_2020_paper.html">**UniPose: Unified Human Pose Estimation in Single Images and Videos**</a>.
</p><br />




<p align="center">
  <img src="https://people.rit.edu/bm3768/images/Unipose_pipeline.png" title="WASPnet architecture for Semantic Segmentation">
  Figure 1: UniPose architecture for single frame pose detection. The input color image of dimensions (HxW) is fed through the ResNet backbone and WASP module to obtain 256 feature channels at reduced resolution by a factor of 8. The decoder module generates K heatmaps, one per joint, at the original resolution, and the locations of the joints are determined by a local max operation.
</p><br />

  
We propose the “Waterfall Atrous Spatial Pyramid” module, shown in Figure 3. WASP is a novel architecture with Atrous Convolutions that is able to leverage both the larger Field-of-View of the Atrous Spatial Pyramid Pooling configuration and the reduced size of the cascade approach.<br />

<p align="center">
  <img src="https://www.mdpi.com/sensors/sensors-19-05361/article_deploy/html/images/sensors-19-05361-g006.png" width=500 title="WASP module"><br />
  Figure 3: WASP Module.
</p><br />

  
Link to the published article at <a href="https://openaccess.thecvf.com/content_CVPR_2020/html/Artacho_UniPose_Unified_Human_Pose_Estimation_in_Single_Images_and_Videos_CVPR_2020_paper.html">CVPR 2020</a>.
</p><br />

**Datasets:**
<p align="justify">
Datasets used in this paper and required for training, validation, and testing can be downloaded directly from the dataset websites below:<br />
  LSP Dataset: https://sam.johnson.io/research/lsp.html<br />
  MPII Dataset: http://human-pose.mpi-inf.mpg.de/<br />
  PennAction Dataset: http://dreamdragon.github.io/PennAction/<br />
  BBC Pose Dataset: https://www.robots.ox.ac.uk/~vgg/data/pose/<br />
</p><br />

**Pre-trained Models:**
<p align="justify">
The pre-trained weights can be downloaded
  <a href="https://drive.google.com/drive/folders/1dPc7AayY2Pi3gjUURgozkuvlab5Vr-9n?usp=sharing">here</a>.
</p><br />


**NEW!: OmniPose: A Multi-Scale Framework for Multi-Person Pose Estimation**
<p align="justify">
Our novel framework for multi-person pose estimation achieves State-of-the-Art results in several datasets. The pre-print of our new method, OmniPose, can be found in the following link: <a href="https://arxiv.org/abs/2103.10180">OmniPose pre-print</a>. Full code for the OmniPose framework is scheduled to be released in the near future.
</p><br />


**Contact:**

<p align="justify">
Bruno Artacho:<br />
  E-mail: bmartacho@mail.rit.edu<br />
  Website: https://www.brunoartacho.com<br />
  
Andreas Savakis:<br />
  E-mail: andreas.savakis@rit.edu<br />
  Website: https://www.rit.edu/directory/axseec-andreas-savakis<br /><br />
</p>

**Citation:**

<p align="justify">
Artacho, B.; Savakis, A. UniPose: Unified Human Pose Estimation in Single Images and Videos. in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2020. <br />

Latex:<br />
@InProceedings{Artacho_2020_CVPR,<br />
  title = {UniPose: Unified Human Pose Estimation in Single Images and Videos},<br />
  author = {Artacho, Bruno and Savakis, Andreas},<br />
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},<br />
  month = {June},<br />
  year = {2020},<br />
}<br />
</p>
