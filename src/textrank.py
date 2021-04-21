# keyphrase_extraction_python
# Code adapted from https://bdewilde.github.io/blog/2014/09/23/intro-to-automatic-keyphrase-extraction/
# @author Loreto Parisi (loretoparisi at gmail dot com)
# Copyright (c) 2021 Loreto Parisi (loretoparisi at gmail dot com)
#

from keyphraseextraction.TextRank import TextRank4Keyword

title = 'EXPLOITING SYNCHRONIZED LYRICS AND VOCAL FEATURES FOR MUSIC EMOTION DETECTION'
abstract = "One of the key points in music recommendation is authoring engaging playlists according to sentiment and emotions. While previous works were mostly based on audio for music discovery and playlists generation, we take advantage of our synchronized lyrics dataset to combine text representations and music features in a novel way; we therefore introduce the Synchronized Lyrics Emotion Dataset. Unlike other approaches that randomly exploited the audio samples and the whole text, our data is split according to the temporal information provided by the synchronization between lyrics and audio. This work shows a comparison between text-based and audio-based deep learning classiﬁcation models using different techniques from Natural Language Processing and Music Information Retrieval domains. From the experiments on audio we conclude that using vocals only, instead of the whole audio data improves the overall performances of the audio classiﬁer. In the lyrics experiments we exploit the state-ofthe-art word representations applied to the main Deep Learning architectures available in literature. In our benchmarks the results show how the Bilinear LSTM classiﬁer with Attention based on fastText word embedding performs better than the CNN applied on audio. "
text = "EXPLOITING SYNCHRONIZED LYRICS AND VOCAL FEATURES FOR \nMUSIC EMOTION DETECTION \n\nABSTRACT \nOne of the key points in music recommendation is authoring engaging playlists according to sentiment and emotions. While previous works were mostly based on audio for music discovery and playlists generation, we take advantage of our synchronized lyrics dataset to combine text representations and music features in a novel way; we therefore introduce the Synchronized Lyrics Emotion Dataset. Unlike other approaches that randomly exploited the audio samples and the whole text, our data is split according to the temporal information provided by the synchronization between lyrics and audio. This work shows a comparison between text-based and audio-based deep learning classiﬁcation models using different techniques from Natural Language Processing and Music Information Retrieval domains. From the experiments on audio we conclude that using vocals only, instead of the whole audio data improves the overall performances of the audio classiﬁer. In the lyrics experiments we exploit the state-ofthe-art word representations applied to the main Deep Learning architectures available in literature. In our benchmarks the results show how the Bilinear LSTM classiﬁer with Attention based on fastText word embedding performs better than the CNN applied on audio. \n\n1. INTRODUCTION \nMusic Emotion Recognition (MER) refers to the task of ﬁnding a relationship between music and human emotions [24,43]. Nowadays, this type of analysis is becoming more and more popular, music streaming providers are ﬁnding very helpful to present users with musical collections organized according to their feelings. The problem of Music Emotion Recognition was proposed for the ﬁrst time in the Music Information Retrieval (MIR) community in 2007, during the annual Music Information Research Evaluation eXchange (MIREX) [14]. Audio and lyrics represent the two main sources from which it is possible to obtain low and high-level features that can accurately describe human moods and emotions perceived while listening to music. An equivalent task can be performed in the area of Natural Language Processing (NLP) analyzing the text information of a song by labeling a sentence, in our case one or more lyrics lines, with the emotion associated to what it expresses. A typical MER approach consists in training \na classi ﬁer using various representations of the acoustical properties of a musical excerpt such as: timbre, rhythm and harmony [21, 26]. Support Vector Machines are employed with good results also for multilabel classi ﬁcation [30], more recently also Convolutional Neural Networks were used in this ﬁeld [45]. Lyrics-based approaches, on the other hand, make use of Recurrent Neural Networks architectures (like LSTM [13]) for performing text classiﬁcation [46, 47]. The idea of using lyrics combined with voice only audio signals is done in [29], where emotion recognition is performed by using textual and speech data, instead of visual ones. Measuring and assigning emotions to music is not a straightforward task: the sentiment/mood associated with a song can be derived by a combination of many features, moreover, emotions expressed by a musical excerpt and by its corresponding lyrics do not always match, also, the annotation of mood tags to a song turns out to be highly changing over the song duration [3] and therefore one song can be associated with more than one emotion [45]. There happens to be no uni ﬁed emotion representation in the ﬁeld of MER, meaning that there is no consensus upon which and how many labels are used and if emotions should be considered as categorical or continuous, moreover, emotion annotation has been carried on in different ways over the years, depending on the study and experiments conducted. For this reason, researches have developed many different approaches and results visualization that is hard to track a precise state-of-the-art for this MIR task [45]. In this work, our focus is on describing various approaches for performing emotion classiﬁcation by analyzing lyrics and audio independently but in a synchronized fashion, as the lyric lines correspond to the portion of audio in which those same lines are sung and the audio is pre-processed using source separation techniques in order to separate the vocal part from the mixture of instruments and retaining the vocal tracks only. \n\n2. RELATED WORKS \nIn this section we provide a description of musical emotion representation and the techniques for performing music emotion classiﬁcation using audio and lyrics, illustrating various word embedding techniques for text classiﬁcation. Finally we detail our proposed approach. \n\n2.1 Representing musical emotions \nMany studies were conducted for the representation of musical emotions also in the ﬁeld of psychology. Despite cross-cultural studies suggesting that there may be universal psychophysical and emotional cues that transcend language and acculturation [24], there exist several problems in recognizing moods from music. In fact, one of the main difﬁculties in recognizing musical mood is the ambiguity of human emotions. Different people perceive and feel emotions induced/expressed by music in many distinct ways. Also, their individual way of expressing them using adjectives is biased by a large number of variables and factors, such as the structure of music, the previous experience of the listener, their training, knowledge and psychological condition [12]. Music-IR systems use either categorical descriptions or parametric models of emotion for classiﬁcation or recognition. Categorical approaches for the representation of emotions comprehend the ﬁnding and the organization of a set of adjectives/tags/labels that are emotional descriptors, based on their relevance and connection with music. One of the ﬁrst studies concerning the aforementioned approach is the one conducted by Hevner and published in 1936, in which the candidates of the experiment were asked to choose from a list of 66 adjectives arranged in 8 groups [12] as shown in Figure 1. Other research, such as the one conducted by Russell [37], suggests that mood can be scaled and measured by a continuum of descriptors. In this scenario, sets of mood descriptors are organized into low-dimensional models, one of those models is the Valence-Arousal (V-A) space (Figure 2), in which emotions are organized on a plane along independent axes of Arousal (intensity, energy) and Valence (pleasantness), ranging from positive to negative. \n2.2 Music Emotion Classiﬁcation \nMER can be approached either as a classiﬁcation or regression problem in which a musical excerpt or a lyrics sentence is annotated with one or multiple emotion labels or with continuous values such as Valence-Arousal. It starts from the employment of certain acoustic features that resemble timbre, rhythm, harmony and other estimators in order to train Support Vector Machines at classifying the moods [30]. Other techniques examine the use of Gaussian Mixture Models [31, 33] and Naive Bayes classi ﬁers. The features involved for training those classi ﬁers are computed based on the short time Fourier transform (STFT) for each frame of the sound. The most used features are the Mel-frequency cepstral coef ﬁcients (MFCC), spectral features such as the spectral centroid and the spectral ﬂux are important for representing the timbral characteristic of the sound [40]. Neural Networks are employed in [11], where the tempo of the song is computed by means of a multiple agents approach and, starting from other features computed on its statistics, a simple BP neural network classiﬁer is trained to detect the mood. It is not trivial to understand which features are more relevant for the task, therefore feature engineering has been recently carried on with the use of deep architectures (known in this context as fea\n\nFigure 1 . Hevner Adjective Clusters. Sixtysix words arranged in eight clusters describing a variety of moods. \n\nFigure 2 . Russell ’s Valence-Arousal Space. A twodimensional space representing mood states as continuous numerical values. The combination of valence-arousal values represent different emotions depending on their coordinates on the 2D space.\n\nture learning) using either spectral representations of the audio (spectrograms or mel-spectrograms), in [5] feeded to a deep Fully Convolutional Networks (FCN) consisting in convolutional and subsampling layers without any fullyconnected layer or directly using the raw audio signal as input to the network classi ﬁer [9]. \nEmotion recognition can also be addressed by using a lyrics-based approach. In [7] the probability of various emotions of a song are computed using Latent Dirichlet Allocation (LDA) based on latent semantic topics. In [34] the Russell ’s emotion model is employed and a keyword-based approach is used for classifying each sentence (verse). \nOther works see the combination of audio-based classiﬁcation with lyrics-based classiﬁcation in order to improve the informative content of their vector representations and therefore the performances of the classiﬁcation, as in [1,28,38,44]. In [8] a 100-dimensional word2vec embedding trained on 1.6 million lyrics is tested comparing several architectures (GRU, LSTM, ConvNets). Not only the uni ﬁed feature set results to be an advantage, but also the synchronized combination of both, as suggested in [8]. In [29] speech and text data are used in a fused manner for emotion recognition. \n2.3 Word Embedding and Text Classiﬁcation \nIn the ﬁeld of NLP, text is usually converted into Bag of Words (BoW), Term FrequencyInverse Document Frequency (TF-IDF) and, more recently, highly complex vector representations. In fact in the last few years, Word Embeddings have become an essential part of any DeepLearning-based Natural Language Processing system representing the state-of-the-art for a large variety of classiﬁcation task models. Word Embeddings are pre-trained on a large corpus and can be ﬁne-tuned to automatically improve their performance by incorporating some general representations. The Word2Vec method based on skipgram [35], had a large impact and enabled ef ﬁcient training of dense word representations and a straightforward integration into downstream models. [23, 27, 42] added subword-level information and augmented word embeddings with character information for their relative applications. Later works [2,17] showed that incorporating pretrained embeddings character n-grams features provides more powerful results than composition functions over individual characters for several NLP tasks. Character ngrams are in particular ef ﬁcient and also form the basis of Facebook ’s fastText classi ﬁer [2, 18, 19]. The most recent approaches [15,36] exploit contextual information extracted from bidirectional Deep Neural Models for which a different representation is assigned to each word and it is a function of the part of text to which the word belongs to, gaining state-of-the-art results for most NLP tasks. [16] achieves relevant results and is essentially a method to enable transfer learning for any NLP task without having to train models from scratch. Regarding the prediction models for text classiﬁcation, LSTM and RNN including all possible model Attention-based variants [47] have repre\ning, text classiﬁcation [46] and machine translation [4]; other works show that CNN can be a good approach to solve NLP task too [22]. In the last few years Transformer [41] outperformed both recurrent and convolutional approaches for language understanding, in particular on machine translation and language modeling. \n2.4 Proposed Approach \nWe built a new emotion dataset containing synchronized lyrics and audio. Our labels consist in 5 discrete crowdbased adjectives, inspired by the Hevner emotion representation retaining just the basics emotions as in [10]. Our aim is to perform emotion classiﬁcation using lyrics and audio independently but in a synchronized manner. We have analyzed the performances of different text embedding methods and used contextual feature extraction such as ELMo and BERT combined with various classi ﬁers. We have exploited novel WaveNet [32, 39] techniques for separating singing voice from the audio and used a Convolutional Neural Network for emotion classiﬁcation. \n\n3. SYNCHRONIZED LYRICS EMOTION DATASET \nPrevious methods combining text and audio for classiﬁcation purposes were randomly analyzing 30 seconds long segments from the middle of the audio ﬁle [33]. Starting from the idea that the mood can change over time in an audio excerpt, as well as a song might express different moods depending on its lyrics and sentences, we exploit our time-synchronized data and build a novel dataset, the Synchronized Lyrics Emotion Dataset , containing synchronized lyrics collected by the Musixmatch platform having start and duration times in which certain lyrics lines are sung. Musical lyrics are the transcribed words of a song, therefore synchronization is a temporal information that establishes a direct connection between the text and its corresponding audio event interval, in other words, synchronizing lyrics is about storing information on the instance of time (in the audio) at which every lyric line starts and ends. Each sample of the dataset consists of 5 values: the track ID, the lyrics, start/end time information related to the audio ﬁle segments and its relative mood label. The 5 collected emotion labels are shown in Table 1 together with their distribution in the dataset. Each audio segment is a slice of music where the corresponding text is sung and it is tagged with a mood label. Since we need a consistent dimension for our audio features, we chose the audio/text segments to be approximately 30 second long. For simplicity, we distinguish three types of segments: intro, synch, outro . The intro is the portion of a song that goes from the beginning of the song until the starting of the ﬁrst sung line. The synch part goes from the beginning of the ﬁrst sung line until the last one. The outro is a segment that starts from the end of the last sung line until the end of the song. Usually, intro and outro do not contain vocals and, in order to ful ﬁl a consistent analysis, we do not take into account those when analyzing the audio, since our goal is to \nsented for years the milestone for solving sequence learn\n"

textRank = TextRank4Keyword()
textRank.analyze(text, candidate_pos = ['NOUN', 'PROPN'], window_size=4, lower=False)
print(textRank.get_keywords(10))



